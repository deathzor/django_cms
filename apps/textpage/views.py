from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse
from .models import *
# Create your views here.

def pageView(request,page=None):
    if (page == None):
     page = "index"
    page = textpage.objects.get(page=page)
    print(page.html);
    template = loader.get_template('textpage/templates/textpage.html')
    title = 'home';
    context = { 'html': page.html,"title":page.title }
    return HttpResponse(template.render(context,request))
