from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    #content kısmında CK editoru kullanmak istediğim için richTextField kullandım. 
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    file_upload = models.FileField(blank=True, null=True, verbose_name="File Upload")
    def __str__(self):
        return self.title



#Kullanıcı yada ziyaretçi yorumları için yeni bir class oluşturduk
#Önce Yorumlarımızı makalenin ID'sine bağladık
#  Admin panelide ise yorumun içeriğini göstererek sonlandırdık.
class ArticleComment(models.Model):
    #related_name kullanmamızın sebebi article alanını Article modeli ile bağladık ve Article.comment diyerek buraya doğrudan erişim sağlayabiliyoruz.
    #Views'da detail kısmında bunun faydasını gördük
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article comment",related_name="comment")
    Name = models.CharField(max_length=50,verbose_name="Name")
    comment = RichTextField()
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self) -> str:
        return self.comment