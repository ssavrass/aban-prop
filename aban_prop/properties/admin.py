# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from properties.models import PropertiesSubmit, Properties

# Register your models here.

admin.site.register(PropertiesSubmit)

admin.site.register(Properties)