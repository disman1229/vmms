from django.contrib import admin

from .models import Vmms

@admin.register(Vmms)
class VmmsAdmin(admin.ModelAdmin):
    list_display = ('id','carModel','VIN','mileage','recipient','sampleDate','returnDate','testProject','testState','transport','park','remarks')
