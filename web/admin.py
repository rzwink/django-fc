from django.contrib import admin

from .models import Contact
from .models import Content
from .models import News
from .models import Product
from .models import Sponsor


@admin.action(description="Inactivate selected")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Activate selected")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "is_active"]
    list_filter = [
        "is_active",
    ]
    search_fields = ["name", "description"]

    actions = [make_active, make_inactive]


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "link", "is_active"]
    list_filter = [
        "is_active",
    ]
    search_fields = ["name", "description"]

    actions = [make_active, make_inactive]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "slug",
        "content",
    ]


@admin.register(Contact)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
    ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "headline",
        "summary",
        "created_on",
    ]
