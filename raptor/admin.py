from django.contrib import admin

# Register your models here.
from .models import Sighting

@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'spotter', 'when', 'status']
    list_filter = ['status', 'created', 'when', 'spotter']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['spotter']
    date_hierarchy = 'when'
    ordering = ['status', 'when']
    show_facets = admin.ShowFacets.ALWAYS

