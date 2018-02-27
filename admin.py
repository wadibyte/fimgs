import os
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import Fimg
# Register your models here.


class FimgInline(GenericTabularInline):
    model = Fimg



class FimgAdminModel(admin.ModelAdmin):
    model = Fimg
    empty_value_display = '-empty-'
    list_filter = ['create_at',]

    list_display = ['create_at', 'id', 'image', 'get_width', 'get_height',
                    'get_ext', 'get_contnent_object']

    list_display_links = ['create_at']

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        super().save_model(request, obj, form, change)

    def get_ext(self, obj):
        name, ext = os.path.splitext(obj.image.name)
        return ext
    get_ext.short_description = 'Ext Type'

    def get_width(self, obj):
        return obj.image.width
    get_width.short_description = 'width'

    def get_height(self, obj):
        return obj.image.height
    get_height.short_description = 'height'

    def get_contnent_object(self, obj):
        if obj.content_object is None:
            return None
        return obj.content_object
    # get_contnent_object.admin_order_field  = 'author'
    get_contnent_object.short_description = 'ContentType Name'


admin.site.register(Fimg, FimgAdminModel)
