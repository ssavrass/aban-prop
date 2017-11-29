
from rest_framework import serializers
from .models import Properties



# class PropertiesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Properties
#         fields = ('id', 'lat', 'lon', 'title', 'address', 'description', 'image')
#         image = 

class PropertiesSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only= True)
	lat = serializers.CharField(read_only= True)
	lon = serializers.CharField(read_only= True)
	title = serializers.CharField(read_only= True)
	address = serializers.CharField(read_only= True)
	description = serializers.CharField(read_only= True)
	image = serializers.CharField(read_only= True)
