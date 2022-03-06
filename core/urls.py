from django.urls import path
from .views import home,join_whatsapp,join_telegram
urlpatterns =[
    path('home/',home, name='home'),
    path('join-whatsapp-group/',join_whatsapp, name='join_whatsapp'),
    path('join-telegram-group/',join_telegram, name='join_telegram'),
]