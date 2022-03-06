from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'home_page/base.html')

    
def join_whatsapp(request):
    return render (request,'home_page/whatsapp_group.html')

def join_telegram(request):
    return render (request,'home_page/telegram.html')