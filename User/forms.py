"""
Kayıt olma / Giriş Yapmak gibi ihtiyacımız olan form sayfaları için 'ÖZEL' olarak oluşturduğumuz forms.py dosyasındayız

"""


from django import forms
from django.forms.widgets import TextInput
from django.http.request import validate_host #DJANGO'nun bizler için özel olarak sunduğu form classını tanımlıyoruz.


class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    
    

#Kendimize özel olarak bir kayıt class oluşturuyoruz fakat oluştururken formlar clasının içerisindeki FORM objesini çağırıyoruz.
class RegisterForm(forms.Form):
    #kendi ihtiyacımız olan form alanları burada tanımlıyoruz. 
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))#arttrs özelliği ile html koda doğrudan müdahele edebiliyoruz. Fakat arttrs kullanabilmek için widgeti mutlaka eklememiz gereklidir!
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'})) #parola girişi olacağı için widget ile bunu belirterek maskeliyoruz.
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-Passowrd', 'class':'form-control'}))
    
    #Form'un içerisinde bulunan bir methottur. Girilen iki parolanın bir birleri ile doğru olup olmadığını kontrol etmemizi sağlamak için kendimize göre
    # Owerwrite yaparak yeniden hazırlıyoruz. Yani form submit edilirken buradaki kontroller yapılıyor. Sorun yoksa form sorunsuz bir şekilde gönderilir.
    # Aksi halde aşşağıda belirttiğimiz hata ile karşı karşıya kalacaktır. 
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")

        if username and password and (password !=repassword):
            raise forms.ValidationError("Password are not matches!")
        values={
            "username":username,
            "password":password
        }
        return values