from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  my_dict = {'insert_me':"Hello form views!"}
  return render(request,'first_app/index.html',context=my_dict)
