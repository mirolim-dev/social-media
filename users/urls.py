from django.urls import path

from .views import home, settings, profile,\
     sign_in, sign_up, account_settings, follow


urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('account_settings/', account_settings, name='account_settings'),

    path('follow/<int:pk>', follow, name='follow'),
]
