from django.contrib import admin
from .models import Forum
# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Forum,ForumAdmin)