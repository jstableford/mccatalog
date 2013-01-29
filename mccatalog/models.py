from django.db import models

class Item(models.Model):
	item_name = models.CharField(max_length=200)
	item_symbol = models.CharField(max_length=5)
	item_id = models.CharField(max_length=20)
	
class Quantity(models.Model):
	item_id = models.ForeignKey(Item)
	minq = models.IntegerField()
	maxq = models.IntegerField()
	quan = models.IntegerField()
