from django.contrib import admin
from .models import *

admin.site.site_header ='адмика Чибиса'
admin.site.index_title = 'mdmmotors.ru'
admin.site.register(Conditions)
admin.site.register(Catalog)

@admin.register(CarModels)
class CarModelsAdmin(admin.ModelAdmin):
    search_fields = ('name',  )




@admin.register(PartBrand)
class PartBrandAdmin(admin.ModelAdmin):
    search_fields = ('name', )

@admin.register(PartItem)
class PartItemAdmin(admin.ModelAdmin):
    search_fields = ('oem','name')
    list_filter = ('category','brand')
    list_display = [ 'name', 'oem','quantaty', 'price',  ]
    list_editable = [ 'quantaty', 'price',]

@admin.register(Contryes)
class ContryesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
#
@admin.register(CarBrands)
class CarBrandsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ( 'name', 'name')

