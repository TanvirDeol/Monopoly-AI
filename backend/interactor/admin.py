from django.contrib import admin
from .models import Interactor

class InteractorAdmin(admin.ModelAdmin):
    list_display = ('pos','money','propertyBought','propertyExpanded','housesBought')

# Register your models here.
admin.site.register(Interactor,InteractorAdmin)
