from django.contrib import admin

# Register your models here.
from .models import Service, ContactRequest, Project

admin.site.register(Service)
admin.site.register(ContactRequest)
admin.site.register(Project)