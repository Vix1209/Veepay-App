from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(models.bulk_sms)
admin.site.register(models.buy_airtime)
admin.site.register(models.cable)
admin.site.register(models.sell_to_us)
admin.site.register(models.SME_data)
admin.site.unregister (Group)

admin.site.site_header = 'Veepay Telecommunications'