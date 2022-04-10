from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,reverse
from . import forms
from django.contrib import messages
from . import models
#Kullanıcıların login olmadan girmemesi gereken sayfaları kontrol amacı ile login required fonksiyonunu dahil ediyoruz
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,("index.html"))

def about (request):
    context= {
        "context":    ["Hasan ",22,"Yazılım Mühendisliği","Siber Güvenlik Uzmanı"]
        }
    return render(request,("about.html"),context)

#Hızlı ve pratik olarak gelen isteğin post ya da get istek olduğunu kontrol ediyoruz. Formumuz valid yani her hangi bir hata almadığında kayıt ettiriyoruz 
#fakat önce formun içerisine makaleyi paylaşan kullanıcının kim olduğunu belirtmemiz gerekiyor bu yüzden formu veritabanına kayıt ettirmiyoruz.
#commit = false diyerek kayıt işlemini askıya alıyoruz ve article tablosundaki author sütununa denk gelicek değerine mevcut kullanıcının olduğunu belirtiyoruz
#daha sonra article.save diyerek verilerimizi başarıyla kayıt edip. Mesajımızı yayınlayarak return redicert ile sayfayı index kısmına gönderimini sağlıyoruz.

#Kullanıcı giriş yapmadan makale eklemeye sayfasına giriş yapmak istediğinde kullanıcı girişi yapması istenilicek
@login_required(login_url="User:login")
def addArticle(request):
    form = forms.ArticleForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Thank you for share your article!")
        return redirect("index")
       
    return render(request,("addArticle.html"),{"form":form})
#Makale detay sayfası için gelen request isteğindeki "id" yi aşşağıda ki parametrede belirtiyoruz. 
#daha sonra article modelinde ki objeleri gelen istekteki id ile model içerisindeki id ye eşitliyoruz ve daha sonra diyoruz ki bütün objeleri değil id ile uyuşan ilk
#objeyi bize getir diyoruz ve bunu detail sayfasına göndererek detayları yayınlıyoruz.
def detailArticle(request,id):
    #Alt satırda yoruma alınan stil verileri getiriyor fakat 
    #Veri yoksa uyarı vermeden ekrana bilgi gönderebiliyor.
    #article = models.Article.objects.filter(id=id).first


    #Yeni Stilde eğer sayfa yoksa ekrana 404 hatası verdiriyirouz.
    #Kullanımı şu şekilde get_object_or_404("Model Adı", id=id) Gelen veri ile modelde bulunan gelmesini istediğimiz veriyi eşitliyoruz
    article=get_object_or_404(models.Article, id=id)
    comments = article.comment.all()
    
    context = {"article":article,
    'comments':comments}
    return render(request,"detail.html",context)
@login_required(login_url="User:login")
def updateArticle(request, id):
    article = get_object_or_404(models.Article, id=id)
    #Once boyle bir id ye sahip makale var mi kontrol ediyoruz daha sonra makale mevcut ise
    #instance ile makalenin bilgilerini forma aktarıyoruz. Özetle instance hayat kurtarır..
    form = forms.ArticleForms(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"{} is published succesfully".format(article.title))

        # article altında ki dashboarda yönlendirmek için  ':' işaretini kullandık. Başka bir örnek: User:Dashboard yani user altındaki dashboarda gitmesini istedim
        return redirect("article:dashboard")
    return render(request,("updateArticle.html"),{"form":form})
@login_required(login_url="User:login")
def deleteArticle(request,id):
    article = get_object_or_404(models.Article,id=id)
    article.delete()
    messages.success(request,"Article was succesfully delete")
    return redirect("article:dashBoard")

 #Dashbord alanında daha önce kullanıcıların kendilerine ait olup yazmış olduğu mesajları gösteriyoruz
 #Bu işlemi önce modelimizi çağırıp model içerisindeki objeyi mevcut kullanıcıların kendilerine ait makalelerini filtrelediğimizi belirtiyoruz. 
 # Bu işlem modelAdi.object.filter(filtrelenmesi istenilen alan adı = request.user) yani isteği yapan kullanıcı şeklinde tanımlıyoruz.
 #Daha sonra ise veriyi dashboard ekranına gönderiyoruz.
@login_required(login_url="User:login")
def dashboard(request):
    articles = models.Article.objects.filter(author = request.user)
    context ={"articles":articles}
    return render(request,("dashboard.html"),context)
    #Dinamik URL için oluşturduklarımız aşşağıda mevcuttur.
    #id gelen istek üzerinde ki ismi döndürmemizi sağlar örneğin .com/article/19 mayıs
    #Selam Bugünki Yazımız: 19 mayıs 
"""def detail (request,id):
    return HttpResponse("Detail: " + str(id))
def detailArticle (request,id):
    return HttpResponse("Merhaba! Bugünki Yazımız: " + id)"""

#articles.html sayfasından arama talebinde bulunulup bulunulmadığı kontrol ediliyor. Eğer arama var ise gelen kelime keyword değişkeninie atanıp
#daha sonra article modelindeki title kısmının içerip (__contains) içermediği kontrol ediliyor. 
#Makale mevcut ise ekrana gönderiliyor. Değil ise articles.html kısmında bulunamadığı ile ilgili uyarı veriliyor.   
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = models.Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{'articles':articles})
    articles = models.Article.objects.all()
    
    
    return render(request,"articles.html",{'articles':articles})



#önce gelen id ile yorumun bulunduğu makale idsi var mı yok mu onu kontrol ediyoruz. 
#Daha sonra gelen isteğin POST isteği olduğunu öğrenip detail.html kısmından
#yorum sahibinin adı ve yorumunu birer değişkene atıyoruz.
#objComment adında oluşturduğumuz bu değişken ile yorum sahibi ve yorumunu modelimizdeki alanlarla eşitliyoruz
#modelimizde bulunan ve article ile bağlantılı olan alanı ise ilk aşamadaki obje kontrolümüzdeki değişkenle eşitleyip kayıt ediyoruz ve 
#bir ekrana bir mesaj yayınlıyoruz.
def comment(request,id):
    article = get_object_or_404(models.Article, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        objComment = models.ArticleComment(Name=name,comment=comment)
        objComment.article=article
        objComment.save()
        messages.success(request,"Your comment published with succesfully. Thank you {}".format(name))
    
    return redirect(reverse("article:detailArticle",kwargs={"id":id}))
        

