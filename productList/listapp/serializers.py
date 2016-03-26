from django.contrib.auth.models import User, Group
from models import ProductList
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class ProductListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductList
		fields = ('product_id', 'product_name','product_url')