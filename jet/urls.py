from django.urls import re_pattern
from django.views.i18n import JavaScriptCatalog

from jet.views import add_bookmark_view, model_lookup_view, remove_bookmark_view, toggle_application_pin_view

javascript_catalog = JavaScriptCatalog.as_view()

app_name = 'jet'

urlpatterns = [
	re_pattern(
		r'^add_bookmark/$',
		add_bookmark_view,
		name='add_bookmark'
	),
	re_pattern(
		r'^remove_bookmark/$',
		remove_bookmark_view,
		name='remove_bookmark'
	),
	re_pattern(
		r'^toggle_application_pin/$',
		toggle_application_pin_view,
		name='toggle_application_pin'
	),
	re_pattern(
		r'^model_lookup/$',
		model_lookup_view,
		name='model_lookup'
	),
	re_pattern(
		r'^jsi18n/$',
		javascript_catalog,
		{'packages': 'django.contrib.admin+jet'},
		name='jsi18n'
	),
]
