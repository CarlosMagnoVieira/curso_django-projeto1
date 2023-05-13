from django.db import models
from django.contrib.auth.models import User

class Language (models.Model):
    language_name = models.CharField(max_length=30)
    language_version = models.CharField(max_length=15)

    def __str__(self):
        return self.language_name+'_'+self.language_version
        

class Commands(models.Model):

    id=models.AutoField(primary_key=True)
    command_name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    slag = models.SlugField()
    sintaxe = models.CharField(max_length=80)
    specifications = models.TextField()
    specifications_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to ='commands/cover/%Y/%m/%d/',blank=True,default='')
    language = models.ForeignKey(Language,on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    fonte= models.CharField(max_length=150)

    def __str__(self):
        return self.command_name+'_'+self.language.language_name


# Create your models here.
