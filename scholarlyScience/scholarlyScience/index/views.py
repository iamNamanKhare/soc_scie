from django.shortcuts import render
from .models import companies


def apphome(request):
    #skill = []
    #for x in range(0, 1):
     #   skill.append(companies.objects.filter(id='{value}'.format(value=x)).first())

    content = {

        'companies': companies.objects.all(),
        'skills':companies.objects.filter(id='{value}'.format(value=str(x) for x in range(0,1))).first()
    }
    return render(request, 'index/home.html', content)
