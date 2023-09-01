from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by word"

    parameter_name = "filter by word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("greate", "Greate"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, queryset):
        # print(queryset[2].review)
        keyword = self.value()
        if keyword == None:
            return queryset
        return queryset.filter(review__contains=keyword)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "review",
        "room",
    )

    list_filter = (
        WordFilter,
        "room",
        "rating",
        "user__is_host",
        "room__category",
    )
