from django import forms
from django.shortcuts import redirect, render
from . import forms
# Create your views here.
#User model ve login olmak için authentication olmak için login classını çağırıyoruz.
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout

#Mesajları yayınlamamız için buraya kütüphanemizden tanımlıyoruz
from django.contrib import messages
#Bir Tık Daha Kısa Yol
def register(request):
    #Gelen requestin POST mu yoksa GET mi olduğunu aşşağıdaki şekilde öğreniyoruz
    #Yani request POST ise form.is_valid()'e uğrayarak direk kontrol edilicek 
    #POST değil ise koşul es geçilip form ile kullanıcıyı direk baş başa bırakıcaz geriye kalan işlemler ise #Uzun Yol ile aynıdır.
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        #kullanıcıya kayıt olduğuna dair bilgi mesajı gönderiyoruz. Gönderilen mesajın kontrolü 'layout.html' kısmında sağlanıyor değişiklikleri oradan sağlayabilirsin!
        messages.success(request,"Welcome!! You Are Successfully Registered!")
        return redirect("index")

    context ={"form":form}
    return render(request,"register.html",context)

def Userlogin (request):
    form = forms.UserLogin(request.POST or None)
    context ={"form":form}
    #Userlogin classı içerisinde clean methodu kullanmadık. Fakat kullanmadık diye form.is_valid() ifadesini kullanamayız diye bir şey yok çünkü
    #clean methodunun kendine has kuralları var biz bunu değiştirmek istediğimizde ya da özelleştirmek istediğimizde çağırarak yapabiliriz. Aksi halde kendi içerisindeki kurallar geçerli olacaktır!
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        User =  authenticate(username=username,password=password)
        if User is None:
            messages.error(request,"Username or Password is not true!")
            return render(request,"index.html")
        messages.success(request,"Again Welcome!")
        login(request,User)
        return redirect("index")

    return render(request,"login.html",context)
def UserLogout(request):
    logout(request)
    messages.success(request,"Logout is succesfull!")
    return redirect("index")





#Uzun Yol
"""

Önce User modelini çağırıyoruz daha sonra şekide A'da ki gibi gelen isteğin POST olup olmadığını kontrol ediyoruz
Eğer gelen istek POST ise istek içerisindeki bilgileri şekil B'deki gibi alıyoruz.
daha sonra forms.py dosyasında bulunan clean methodunun doğru olup olmadığını şekil C'deki gibi kontrol ediyoruz.
doğru ise hemen gelen POST isteğindeki kullanıcı adı ve şifreleri şekil D' deki gibi alıyoruz.
Yalnız! Parolayı şekil Ê'deki gibi şifrelemeyi unutmuyoruz ve daha sonra
eklenilen bir diğer model olan şekil F' yi şekil G' de ki gibi kullanarak login oluyor ve son olarak sayfamızı redirect ile yönlendiriyoruz!


Fakat! gelen istek POST olup ama clean methodu true değil ise kullanıcıyı geri register sayfasına yönlendirip hata mesajı iletiyoruz. ( Şekil H)

eğer gelen istek GET methodu ise direk kullanıcıyı boş form sayfası ile baş başa bırakıyoruz.

from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login #F


def register (request):
    
    if request.method =="POST": # A
        form = forms.RegisterForm(request.POST) # B
        if form.is_valid():# C
            username = form.cleaned_data.get("username") # D
            password = form.cleaned_data.get("password") # D
            NewUser = User(username = username)
            NewUser.set_password(password) # Ê
            NewUser.save() # burada kullanıcıyı kayıt ediyoruz.
            dj_login(request, NewUser) # G
            return redirect("index") #Burada yönlendiriyoruz.
        
        
        value ={"form":form} #H
        return render(request,"register.html",value)
            
    form=forms.RegisterForm() # Burada Methodun GET ile geldiğini öğrenerek kullanıcıya boş form sayfası yönlendiriyoruz.
    value ={"form":form}
    return render(request,"register.html",value)






"""