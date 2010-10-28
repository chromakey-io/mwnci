import settings

def raise_404(method):
	def wrap(*args, **kwargs):
		from django.core.exceptions import ObjectDoesNotExist
		from django.http import Http404
		try:
			return method(*args, **kwargs)
		except ObjectDoesNotExist, ex:
			raise Http404(ex.message)
	return wrap