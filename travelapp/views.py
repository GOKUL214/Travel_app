from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Meet


# Create your views here.



def demo(request):
    obj = Place.objects.all()
    obj1 = Meet.objects.all()

    return render(request,'index.html', {'result':obj, 'res':obj1})

# def addition(request):
#
#     return render(request,'index.html')

