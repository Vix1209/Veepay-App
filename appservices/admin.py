from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    
    
admin.site.register(models.bulk_sms)
admin.site.register(models.buy_airtime)
admin.site.register(models.cable)
admin.site.register(models.sell_to_us)
admin.site.register(models.SME_data)
admin.site.register(models.Newsletter, NewsletterAdmin)
# admin.site.register(MailMessage)
admin.site.unregister (Group)

admin.site.site_header = 'Veepay Telecommunications'


