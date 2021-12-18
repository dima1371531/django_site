from django.contrib import admin
from .models import Users,Product,Cart

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Cart)