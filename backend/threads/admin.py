from django.contrib import admin
from .models import Thread
# Register your models here.

class ThreadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thread,ThreadAdmin)