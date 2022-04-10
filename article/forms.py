from django.forms import ModelForm, fields
from . import models

class ArticleForms(ModelForm):
    class Meta:
        model=models.Article
        fields=["title","content","file_upload"]