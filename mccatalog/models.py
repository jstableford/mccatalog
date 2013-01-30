from django.db import models

class Item(models.Model):
	item_name = models.CharField(max_length=200)
	item_symbol = models.CharField(max_length=5)
	item_id = models.CharField(max_length=20)
	def __unicode__(self):
		return self.item_name
		
class Quantity(models.Model):
	item = models.ForeignKey(Item, related_name='name')
	minq = models.IntegerField()
	maxq = models.IntegerField()
	quan = models.IntegerField()
	def __unicode__(self):
		return str(self.item_id)
