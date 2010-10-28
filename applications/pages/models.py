from django.db import models
from django.core.urlresolvers import reverse

class Type(models.Model):
    name = models.CharField(max_length=255)
    path = models.SlugField(max_length=50)
    order = models.IntegerField(default = 0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
		return self.name
    
    def main_page(self):
        return self.page_set.get(order=0)
    
    def save(self):
        self.path = self.path.lower()
        super(Type, self).save()

class Theme(models.Model):
    name = models.CharField(max_length=255)
    template = models.FileField(upload_to='templates/')

    def __unicode__(self):
        return self.name

class Widget(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    href = models.URLField(max_length=1024, blank=True)

    image = models.FileField(upload_to='uploaded-images/', blank=True)
    html = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    active = models.BooleanField(default=False, 
        help_text="Check this box to make the page active... please ensure there is only one active page with each path.")

    order = models.IntegerField(default=0)

    name = models.CharField(max_length=255, help_text="Appears in links to page and url-patterns")
    title = models.CharField(max_length=255, help_text="Page Title")

    body = models.TextField(blank=True)

    path = models.SlugField(blank=True, max_length=50,
        help_text="This is the url path for the page.")

    type = models.ForeignKey(Type, null=True, blank=True)      

    theme = models.ForeignKey(Theme, null=True, blank=True)
    
    widget = models.ManyToManyField(Widget, through = "WidgetPosition")

    extra_style = models.TextField(blank=True)

    creation_date = models.DateField(auto_now_add=True)

    def left(self):
        return self.widget.filter(widgetposition__position = 1)
    
    def right(self):
        return self.widget.filter(widgetposition__position = 2)

    def center(self):
        return self.widget.filter(widgetposition__position = 3)

    def save(self):
        self.path = self.path.lower()
        super(Page, self).save()
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        if self.type and self.path:
            url = reverse('sub-page', kwargs={
                'type':self.type.path,
                'path':self.path,
                })
        elif self.type:
            url = reverse('page', kwargs={
                'path': self.type.path,
            })
        else:
            url = reverse('page', kwargs={
                'path': self.path,
            })
        return url
    
    def get_related_pages(self):
        return self.type.page_set.exclude(id = self.id)

    class Meta:
        unique_together = ['path', 'active', 'type', 'order']

class WidgetPosition(models.Model):
    widget = models.ForeignKey(Widget)
    page = models.ForeignKey(Page)

    position = models.PositiveSmallIntegerField(choices = ((1, 'left'), (2, 'right'), (3, 'center')), default = 3)
    order = models.IntegerField(default = 0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.page.name + ' - ' + self.widget.name