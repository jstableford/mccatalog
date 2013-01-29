from django.http import HttpResponse
from datetime import datetime
from django.conf import settings
from django.template import Context, loader
from django.core.cache import cache
from models import Item, Quantity
import re

def home(request):
	list_of_items = Item.objects.all()
	
	t = loader.get_template('index.html')
	c = Context({'list_of_items': list_of_items,})
	return HttpResponse(t.render(c))
