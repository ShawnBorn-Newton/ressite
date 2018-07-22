from django.shortcuts import render
from django.http import HttpResponse

def Help(request):
  help_dict = {'insert_me':'Help Page'}
  return render(request,'Help/Help.html',context=help_dict)