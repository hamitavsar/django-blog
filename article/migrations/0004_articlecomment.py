# Generated by Django 3.1.5 on 2021-12-03 11:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20211126_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('comment', ckeditor.fields.RichTextField()),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article.article', verbose_name='Article comment')),
            ],
        ),
    ]
