from email.mime import application
from django.contrib import admin
from .models import slot,Application
# Register your models here.

admin.site.register(slot)
admin.site.register(Application)