from django.contrib import admin
from .models import Language, Commands

class LanguageAdmin(admin.ModelAdmin):
    ...

@admin.register(Commands)
class CommandsAdmin(admin.ModelAdmin):
      ...       
    
admin.site.register(Language,LanguageAdmin)
