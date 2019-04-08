from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import * 
# Create your views here.
def fitView(request,fitid):
    fit = fitting.objects.get(id=fitid)
    fitting_array = fit.parseEFT()
    template = loader.get_template('shipfit.html')
    context = { 'ship': fitting_array }
    return HttpResponse(template.render(context,request))

def doctrineView(request,doctrineId=None):
    if (doctrineId == None):
       doctrinelist = doctrine.objects.all().values()
       template = loader.get_template('doctrine.html')
       context = {'doctrine':doctrinelist}
       return HttpResponse(template.render(context,request))
    else:
       shipobjects = fitting.objects.filter(doctrine=doctrineId)
       shiplist = []
       for item in shipobjects:
           shiplist.append({"id":item.id,"name":item.parseEFT()['name']})


       template = loader.get_template('doctrine_ships.html')
       context = {'ships': shiplist }
       return HttpResponse(template.render(context,request))

