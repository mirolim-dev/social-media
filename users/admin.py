from django.contrib import admin
from .models import User, Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortage']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'number_of_followers', 'number_of_followings']


admin.site.register(User, UserAdmin)
admin.site.register(Language, LanguageAdmin)