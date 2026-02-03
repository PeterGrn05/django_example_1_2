from django.contrib import admin
from products.models import Genre, Book, Publisher, Supplier, Unit


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ...

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    ...

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']