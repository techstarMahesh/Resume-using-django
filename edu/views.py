from django.shortcuts import render

# Create your views here.
def skills(request):
    return render(request, 'edu/skills.html', {'title': 'Skills', 'skills':'active'})