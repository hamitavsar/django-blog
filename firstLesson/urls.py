"""firstLesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.contrib import admin
from django.urls import path, include
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index,name="index"),
    path('about/', views.about,name="about" ),
    #aşşağıda yaptığımız kısım ile articles modülü içerisinde oluşturduğumuz 'urls.py' klasörüne  '.com/articles' ile gelen istekleri yönlendirir
    #bu sayede hızlı ve daha derli toplu bir url kontrolü sağlamış oluruz.
    path('articles/', include('article.urls'),name="articles"),
    path('user/', include('User.urls'),name="user")

    # Dinamik url tanımlarken oluşturduğum şekli aşşağıda verdim. Eğer dinamik yapıyı int olarak tanımlanırsa view kısmında kullanılmak istendiğinde int olarak 
    # gittiğini bilmek gerekli
    # 
   # path('detail/<int:id>',views.detail,name="detail"),
   # path('Article/<str:id>',views.detailArticle,name="detailArticle")
]
#We have to add their for upload file.
#You are learn more information about file upload from https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
