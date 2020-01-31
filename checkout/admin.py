from django.contrib import admin
from .models import Order, OrderLineItem


#class inherits from Django admin TabularInline class
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

# class inherits from Django ModelAdmin class
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

# Order models registered here to allow editing in the admin panel
admin.site.register(Order, OrderAdmin)
