from django.contrib import admin
from HW_app.models import Category, Product, Review


# Register your models here.

class ReviewInline(admin.StackedInline):
    model = Review
    fields = 'text'.split()


class ProductInline(admin.StackedInline):
    model = Product
    fields = 'title'.split()


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = 'title description price category'.split()
    search_fields = 'title'.split()
    list_filter = 'category'.split()
    list_editable = 'description price'.split()
    inlines = [ReviewInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = 'author text date'.split()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
