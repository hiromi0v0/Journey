from django.contrib import admin

from .models import Country,Attribute,PhotoPost

class CountryAdmin(admin.ModelAdmin):
    list_display=('id','country_name')
    list_display_links=('id','country_name')


# class AttributeAdmin(admin.ModelAdmin):
#     list_display=('id','happy')
#     list_display_links=('id','happy')


class PhotoPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

admin.site.register(Country,CountryAdmin)
admin.site.register(Attribute)
admin.site.register(PhotoPost,PhotoPostAdmin)

# Register your models here.

