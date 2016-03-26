from __future__ import unicode_literals

from django.db import models

class ProductList(models.Model):	#inheritance, parent class : models.Model
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_url = models.CharField(max_length=500)
    class Meta:
    	db_table = u'tbl_product_list'
    	app_label = 'listapp'

# Create your models here.
