from django.template import RequestContext
from django.shortcuts import render_to_response
from shortcuts import raise_404

from pages.models import Page, Type

@raise_404
def page(request, path='', type=None):
    pages = None
    if type:
        type = Type.objects.get(path = type)
        page = Page.objects.get(path = path, type = type)
        pages = Page.objects.filter(type = type)
    else:
        try:
            page = Page.objects.get(path = path, type = None)
        except Page.DoesNotExist:
            type = Type.objects.get(path = path)
            page = Page.objects.get(path = '', type = type)

    if page.theme:
        template = page.theme.template.path
    else:
        template = 'pages/page.html'

    types = Type.objects.all()
    active_types = []
    for type in types:
        if type.page_set.filter(path = '', active=True):
            active_types.append(type)

    return render_to_response(template, {'page':page, 'types':active_types, 'pages':pages},
        context_instance=RequestContext(request))
