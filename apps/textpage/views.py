from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse
from .models import *
# Create your views here.

def pageView(request,page=None):
    if (page == None):
     page = "index"
    page = textpage.objects.get(page=page)
    #menustructure = menuitem.object.get(parent=None)
    menuobject = menuitem.objects.filter(parent=None)
    menu = menuobject.values()
    for item in menu:
        item['page'] = textpage.objects.get(id=item['page_id']).page
    template = loader.get_template('textpage/templates/textpage.html')
    title = 'home';
    context = { 'html': page.html,"title":page.title, 'menu':menu}
    return HttpResponse(template.render(context,request))
