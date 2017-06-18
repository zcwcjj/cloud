from django.contrib import admin
from .models import *
from django.contrib.admin.utils import flatten_fieldsets
from django.forms import ModelForm
from django.forms.widgets import Select 


# Register your models here.

class MySelect(Select):
    def __init__(self, attrs=None, choices=()):
        all = Collectpoint_type.objects.all()
        dic = []
        for x in all:
            dic.append((str(x.id), x.remark))
        
        super(MySelect, self).__init__(attrs, tuple(dic))

    

        
    


class Collectpoint_type_inline(admin.TabularInline):
    model = Collectpoint_type
    extra = 3




@admin.register(Equipment_class)
class Equipment_class_admin(admin.ModelAdmin):
    exclude = []
    inlines = [Collectpoint_type_inline]


    

class WebAcess_tag_modelform(ModelForm):
    class Meta:
        model = WebAcess_tag
        exclude = []
        widgets = {
            'tag_name':MySelect(
            attrs = {
            'class':'unique'
            })
        }


class WebAcess_tag_inline(admin.TabularInline):
    model = WebAcess_tag
    def get_min_num(self, request, obj=None, **kwargs):
            """Hook for customizing the min number of inline forms."""
            
            return 0

    def get_max_num(self, request, obj=None, **kwargs):
        """Hook for customizing the max number of extra inline forms."""
        if obj is not None:
            
            return  Collectpoint_type.objects.filter(owner_equipment_class__id=obj.id).count()
            #return obj.
        return 0

    form = WebAcess_tag_modelform

    readonly_fields = ('tag_from_type',)



@admin.register(Equipment)
class Equiment_admin(admin.ModelAdmin):
    exclude = []
    inlines = [WebAcess_tag_inline]

