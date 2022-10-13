from django.contrib import admin

# Register models.your models here.
from main import models


admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductTag)

