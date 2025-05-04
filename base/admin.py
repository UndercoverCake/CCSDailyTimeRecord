from django.contrib import admin
from .models import userTime, TimeEntry, Holiday, MakeUpClass

# Register your models here.
admin.site.register(userTime)
admin.site.register(TimeEntry)
admin.site.register(Holiday)
admin.site.register(MakeUpClass)