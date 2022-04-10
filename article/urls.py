"""
Oluşturduğumuz bu klasörde ana dosyadan gelen isteklerin '.com/articles' devamını burada kontrol altında tutarız.

 örneğin: '.com/articles' a kadar olanlar doğrudan buraya yönlendirilir 'articles' dan sonra ne talep edildiyse aşşağıda kontrol edilir ve karşılığına yönlendirilir.

 '.com/articles/create-new-article' create-new-article buradan var mı yok mu kontrol edilir eğer öyle bir url mevcut ise yönlendirilir yoksa 404 ile kullanıcıya böyle
 bir sayfanın olmadığını belirtiriz.

"""


from django.urls import path
from . import views

app_name ="article"

urlpatterns=[
    path('refresh/', views.index, name="refresh"),
    path('dashboard/',views.dashboard, name="dashBoard"),
    path('newArticle/',views.addArticle, name="addArticle"),
    path('detailArticle/<int:id>',views.detailArticle, name="detailArticle"),
    path('updateArticle/<int:id>',views.updateArticle, name="updateArticle"),
    path('deleteArticle/<int:id>',views.deleteArticle, name="deleteArticle"),
    path('commentArticle/<int:id>', views.comment,name="commentArticle"),
    path('',views.articles, name=""),

]