from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Band, Album, Song, Dates

admin.site.register([Band,Album,Song,Dates])