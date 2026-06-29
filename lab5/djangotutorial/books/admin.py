from django.contrib import admin
from .models import ISBN, Book, Category

# Register your models here.
# admin.site.register(Book)
admin.site.register(Category)


# admin.site.register(ISBN)
class ISBNInLine(admin.StackedInline):
    model = ISBN


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ISBNInLine]
