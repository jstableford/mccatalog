from django.http import HttpResponse
from datetime import datetime
from django.conf import settings
from django.template import Context, loader
from django.core.cache import cache
from models import Item, Quantity
import re

def getQuan(name):
	query = Quantity.objects.filter(item__item_name__contains=name)
	return query.values_list()[0][4]

def home(request):
	dic = {}
	list_of_items = Item.objects.all()
	for item in list_of_items:
		name = item.item_name
		quantity = getQuan(name)
		dic[name] = quantity

	
	t = loader.get_template('index.html')
	c = Context({'list_of_items': list_of_items,
				'dic': dic,})
	return HttpResponse(t.render(c))

def getQuanBySymbol(request):
	if request.method == 'GET':
		q = request.GET
	elif request.method == 'POST':
		q = request.POST
	sym = q.__getitem__('sym')
	testprefix = "\nThe quantity is: "	
	query = Quantity.objects.filter(item__item_symbol__exact=sym)
	return HttpResponse(query.values_list()[0][4])

def updateQuanBySymbol(request):
	if request.method == 'GET':
		q = request.GET
	elif request.method == 'POST':
		q = request.POST
	sym = q.__getitem__('sym')
	num = q.__getitem__('num')
# code to come
