from django.shortcuts import render
from .models import companies


def apphome(request):
    
    content = {

        'companies': companies.objects.all()
    }
    return render(request, 'index/home.html', content)
