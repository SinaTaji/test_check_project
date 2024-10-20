from django.contrib import admin
from .models import Staff, EntryAndExit


class EntryAndExitInline(admin.TabularInline):
    model = EntryAndExit
    extra = 0
    fields = ['day', 'entry', 'exit']
    readonly_fields = ['day', 'entry', 'exit']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    inlines = [EntryAndExitInline]
    ordering = ('first_name', 'last_name')

