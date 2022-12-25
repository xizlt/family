from django.contrib import admin

from people.models import People


@admin.register(People)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

