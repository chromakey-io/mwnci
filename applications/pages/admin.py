from django.contrib import admin
from pages.models import *

admin.site.register(Type)
admin.site.register(Theme)
admin.site.register(Widget)
admin.site.register(Page)
admin.site.register(WidgetPosition)