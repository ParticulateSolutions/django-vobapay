from django.contrib import admin
from .models import VobapayTransaction


class VobapayTransactionAdmin(admin.ModelAdmin):
    list_display = ('merchant_tx_id', 'reference', 'latest_response_code',)
    ordering = ('-created_at',)
    fields = ('merchant_tx_id', 'reference',)
    search_fields = ('merchant_tx_id', 'reference')



admin.site.register(VobapayTransaction, VobapayTransactionAdmin)
