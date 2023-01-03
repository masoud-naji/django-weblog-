from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse("Hello, This is Home.")
   return render(request,'homepage.html')


def about(request):
  #  return HttpResponse("Hello, This is About.")
    return render(request,'about.html')


