from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Product, RetailNode


class CityFilter(SimpleListFilter):
    title = "Город"
    parameter_name = "city"

    def lookups(self, request, model_admin):
        cities = RetailNode.objects.values_list("contacts__city", flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city=self.value())
        return queryset


@admin.register(RetailNode)
class RetailNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "supplier", "debt", "created_at"]
    list_filter = [CityFilter]
    search_fields = ["name", "contacts__city"]

    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, "Задолженность успешно обнулена.")

    clear_debt.short_description = "Обнулить задолженность у выбранных объектов"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "model", "release_date", "node"]
