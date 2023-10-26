from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','brand','labels')
    list_filter = ('name','price','category','brand','labels')
    search_fields = ('name','description')
    class Meta:
        ordering = ('id','name','price')

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Feedback)
admin.site.register(SiteInfo)
admin.site.register(Ad)
admin.site.register(Brand)

admin.site.register(Cart)
admin.site.register(ProductReviews)
admin.site.register(Checkout)