from django.urls import re_path
from django.views.i18n import JavaScriptCatalog

from jet.dashboard import dashboard
from jet.dashboard.views import UpdateDashboardModuleView, add_user_dashboard_module_view, load_dashboard_module_view, \
	remove_dashboard_module_view, reset_dashboard_view, update_dashboard_module_collapse_view, \
	update_dashboard_modules_view

javascript_catalog = JavaScriptCatalog.as_view()

app_name = 'dashboard'

urlpatterns = [
	re_path(
		r'^module/(?P<pk>\d+)/$',
		UpdateDashboardModuleView.as_view(),
		name='update_module'
	),
	re_path(
		r'^update_dashboard_modules/$',
		update_dashboard_modules_view,
		name='update_dashboard_modules'
	),
	re_path(
		r'^add_user_dashboard_module/$',
		add_user_dashboard_module_view,
		name='add_user_dashboard_module'
	),
	re_path(
		r'^update_dashboard_module_collapse/$',
		update_dashboard_module_collapse_view,
		name='update_dashboard_module_collapse'
	),
	re_path(
		r'^remove_dashboard_module/$',
		remove_dashboard_module_view,
		name='remove_dashboard_module'
	),
	re_path(
		r'^load_dashboard_module/(?P<pk>\d+)/$',
		load_dashboard_module_view,
		name='load_dashboard_module'
	),
	re_path(
		r'^reset_dashboard/$',
		reset_dashboard_view,
		name='reset_dashboard'
	),
	re_path(
		r'^jsi18n/$',
		javascript_catalog,
		{'packages': 'jet'},
		name='jsi18n'
	),
]

urlpatterns += dashboard.urls.get_urls()

