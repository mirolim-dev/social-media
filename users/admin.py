from django.contrib import admin
from .models import User, Language, Contact, SocialMedia

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortage']


class SocialMediaAdmin(admin.TabularInline):
    model = SocialMedia
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'number_of_followers', 'number_of_followings']
    inlines = [SocialMediaAdmin]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'email', 'website']

admin.site.register(User, UserAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Contact, ContactAdmin)