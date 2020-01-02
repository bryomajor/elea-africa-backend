from django.contrib import admin
from .models import Event, Contact, EventImage

# Register your models here.
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3

class EventAdmin(admin.ModelAdmin):
    inlines = [ EventImageInline, ]

admin.site.register(Event, EventAdmin)
admin.site.register(Contact)

admin.site.site_header = "Elea Africa Backend"
