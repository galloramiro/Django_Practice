from django.contrib import admin
from .models import SmgQuotesTable
# Register your models here.

class SmgQuotesTableAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('composite','smg01', 'smg02', 'smg10', 'smg20', 'smg30', 'smg40', 'smg50', 'smg60', 'smg70')
    search_fields = ('composite',)
    list_filter = ('composite',)


admin.site.register(SmgQuotesTable, SmgQuotesTableAdmin)
