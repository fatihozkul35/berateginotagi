from django.contrib import admin

# Register your models here.
from .models import Category, Menu, Slider, Appconf, About

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'name',)
    ordering = ['position']

admin.site.register(Category, CategoryAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'price',)
    ordering = ['position']

admin.site.register(Menu, MenuAdmin)
admin.site.register(Appconf)
admin.site.register(Slider)
admin.site.register(About)
