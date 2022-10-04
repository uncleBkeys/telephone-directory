from django.shortcuts import render
from urllib import request
from django.shortcuts import render

# Create your views here.
def homepage(request):
    context= {
        'title': 'Homepage'
    }
    return render(request, 'directory/index.html', context)

def amendpage(request):
    context={
        'title': 'Amendpage'
    }
    return render(request, 'director/amend.html', context)

    
def insertpage(request):
    context={
        'title': 'Insertpage'
    }
    return render(request, 'director/insert.html', context)

def removepage(request):
    context={
        'title': 'removepage'
    }
    return render(request, 'director/remove.html', context)