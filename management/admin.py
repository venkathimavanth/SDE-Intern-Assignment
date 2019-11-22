from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(EntryModel)
admin.site.register(ExitModel)
admin.site.register(Host)
