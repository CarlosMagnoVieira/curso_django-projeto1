from django.db import models
from django.contrib.auth.models import User

class Language (models.Model):
    language_name = models.CharField(max_length=30)
    language_version = models.CharField(max_length=15)

class Commands(models.Model):

    command_name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    slag = models.SlugField()
    sintaxe = models.CharField(max_length=80)
    specifications = models.TextField()
    specifications_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to = 'commands/cover/%Y/%m/%d/')
    language = models.ForeignKey(Language,on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)


# Create your models here.
