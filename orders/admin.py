from django.contrib import admin
from .models import Orders
# Register your models here.
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity']
    list_filter = ['created_at', 'order_status', 'size']