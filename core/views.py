from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html', {'title': 'Home', 'home':'active'})


def contact(request):
    return render(request, 'core/contact.html',{'title': 'Contact', 'contact':'active'})