from django.contrib import admin
from.models import*
# Register your models here.
class name(admin.ModelAdmin):
    list_display=("Firstname","Lastname","Email","Password","ConfirmPassword","DOB","Gender")
admin.site.register(users,name)