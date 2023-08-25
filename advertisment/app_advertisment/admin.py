from django.contrib import admin
from advertisment.app_auth.models import Advertisement
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction', 'get_html_image']
    list_filter =  ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)