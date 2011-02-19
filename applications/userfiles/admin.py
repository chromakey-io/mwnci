from django.contrib import admin
from userfiles.models import File, Type

class FileAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    search_fields = ['name']
    list_filter = ['type']

admin.site.register(File, FileAdmin)
admin.site.register(Type)