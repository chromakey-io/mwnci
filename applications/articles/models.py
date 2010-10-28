from django.db import models
from pages.models import Widget

class Page(models.Model):
    active = models.BooleanField(default=False, 
        help_text="Check this box to make the article active.")

    title = models.CharField(max_length=255, help_text="Page Title")

    body = models.TextField(blank=True)

    widget = models.ForeignKey(Widget, null=True, blank=True)

    creation_date = models.DateField(auto_now_add=True)