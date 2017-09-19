from django.contrib import admin
from .models import *







# Admin panel actions: Publish, Draft, Feature, Unfeature
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark elements as published"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark elements as draft"

def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)
make_featured.short_description = "Mark as featured content"

def make_unfeatured(modeladmin, request, queryset):
    queryset.update(destaque=False)
make_unfeatured.short_description = "Unmark as featured content"

#____________________________________________________








# The admin class for the Doc model
# fields are self-explanatory
class DocAdmin(admin.ModelAdmin):
    ordering = ['-publishedDate']
    list_display = ['title', 'author', 'slug', 'language', 'programmingLanguage','updatedDate','status']
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_draft, make_published]


# Color admin class to be featured alongside the Project model
class ColorInLine(admin.TabularInline):
    model = Color

# Photo admin class to be featured alongside the Project model
class PhotoInLine(admin.TabularInline):
    model = Photo

# Person admin class featuring model actions
class PersonAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'position', 'github_username']
    actions = [make_published, make_draft]
    short_description = 'name'

# Project admin class featuring the Color model and model actions
class PortfolioProjectAdmin(admin.ModelAdmin):
    ordering = ['-publishedDate']
    list_display = ['title', 'author', 'client', 'type', 'publishedDate', 'status', 'featured']
    actions = [make_featured, make_draft, make_published, make_unfeatured]
    inlines = [ ColorInLine, PhotoInLine ]
    prepopulated_fields = {"slug": ("title",)}
###___________________________________________

















# Registering Project and Person admin classes...
admin.site.site_header = "Ekletik Studios"
admin.site.register(Doc, DocAdmin)
admin.site.register(PortfolioProject, PortfolioProjectAdmin)
# admin.site.register(Person, PersonAdmin)
# admin.site.register(FeaturedHeader)