from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Store

class StoreResource(resources.ModelResource):
	class Meta:
		model = Store
		fields = ('id', 'name', 'location', 'number')
		export_order = fields


class StoreAdmin(ImportExportModelAdmin):
	fields = ('name', 'location', 'number')
	list_display = ('id', 'name', 'location', 'number')
	resource_class = StoreResource


admin.site.register(Store, StoreAdmin)
