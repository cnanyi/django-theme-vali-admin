from django.contrib import admin
from .models import *
from vali.decorator import vali_models_group
# Register your models here.


@vali_models_group('DemoGroup1')
@admin.register(MainModel)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


@vali_models_group('DemoGroup2')
@admin.register(PersonModel)
class PersonAdmin(admin.ModelAdmin):
    pass


@vali_models_group('DemoGroup2')
@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    pass


@vali_models_group('DemoGroup3')
@admin.register(Prop1, Prop2)
class PropsAdmin(admin.ModelAdmin):
    pass


# this is no group
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass

