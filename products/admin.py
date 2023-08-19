from django.contrib import admin
from .models import Product, Category, SubCategory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        # 'photographer',
        'price',
        'image',
    )

    exclude = ('sku',)

    def save_model(self, request, obj, form, change):
        if not obj.sku:
            obj.sku = Product.generate_sku()
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
