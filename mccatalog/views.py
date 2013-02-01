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
	query = cache.get( sym )
	if query:
		return HttpResponse(query.values_list()[0][4])
	try:
		query = Quantity.objects.filter(item__item_symbol__exact=sym)
		cache.set( sym, query, settings.CACHE_TIMEOUT )
		return HttpResponse(query.values_list()[0][4])		
	except IndexError:
		return HttpResponse()

def updateQuanBySymbol(request):
	if request.method == 'GET':
		q = request.GET
	elif request.method == 'POST':
		q = request.POST
	sym = q.__getitem__('sym')
	num = q.__getitem__('num')
	item = Quantity.objects.filter(item__item_symbol__exact=sym)
	item.values('quan').update(quan=num)
	return HttpResponse()
	
def addSymbol(request):
	if request.method == 'GET':
		q = request.GET
	elif request.method == 'POST':
		q = request.POST
	sym = q.__getitem__('sym')
	name = q.__getitem__('name')
	iid = q.__getitem__('iid')
	this_item = Item(item_name=name, item_symbol=sym, item_id=iid)
	try:
		this_item.save()
		quantity = Quantity(maxq=100, minq=1, item=this_item, quan=0)
		quantity.save()
	except NameError:
		return HttpResponse()
	return HttpResponse()
