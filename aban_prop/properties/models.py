# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Properties(models.Model):

    
    lat = models.TextField(default = "")
    lon = models.TextField(default = "")
    title = models.TextField(default = "")
    address = models.TextField(default = "")
    description = models.TextField(default = "")
    image = models.ImageField(default = 'properties/static/images/no-img.png', upload_to = 'properties/static/images')
    
    def __str__(self):
       return self.title

    @classmethod
    def create(cls, lat, lon, title, address, description, image):
        properties = cls(lat = lat, lon = lon, title = title, address = address, description = description, image = image)
        return properties
    # class Meta:
    #     unique_together = ('info_hash','title')
    #     indexes = [
    #         models.Index(fields=['info_hash']),
            
    #     ]

class PropertiesSubmit(models.Model):

    
    lat = models.TextField(default = "")
    lon = models.TextField(default = "")
    title = models.TextField(default = "")
    address = models.TextField(default = "")
    description = models.TextField(default = "")
    image = models.ImageField(default = 'properties/static/images/no-img.png', upload_to = 'properties/static/images')
    def __str__(self):
       return self.title

    @classmethod
    def create(cls, lat, lon, title, address, description, image):
        properties = cls(title = title, address = address, description = description, image = image)
        return properties
    # class Meta:
    #     unique_together = ('info_hash','title')
    #     indexes = [
    #         models.Index(fields=['info_hash']),
            
    #     ]
   