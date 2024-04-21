from django.contrib import admin

from .models import Menu, MenuItem


admin.site.register(Menu)

# @admin.register(Menu)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = 'name'
#     search_fields = 'name'


admin.site.register(MenuItem)

# @admin.register(MenuItem)
# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     search_fields = 'name'
