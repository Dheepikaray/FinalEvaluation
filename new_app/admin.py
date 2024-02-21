from django.contrib import admin

# Register your models here.
from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Register)
admin.site.register(models.Publisher)
admin.site.register(models.Customer)
admin.site.register(models.blog)

