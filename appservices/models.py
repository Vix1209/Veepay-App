from django.db import models

# Create your models here.


NETWORK = (
    ('MTN',' MTN'),
    ('GLO', 'GLO'),
    ('AIRTEL', 'AIRTEL'),
    ('9MOBILE', '9MOBILE')
)

BILLER = (
    ('GOtv', 'GOtv'),
    ('StarTimes', 'StarTimes'),
    ('DSTV', 'DSTV'),
    ('Showmax', 'Showmax'),
    ('IROKOTV', 'IROKOTV')
)
# Create your models here.

class SME_data (models.Model):
    network = models.CharField(max_length=20, choices=NETWORK, null=True )
    phone = models.IntegerField( null=True )
    amount = models.IntegerField( null=True)
    data_plan =  models.CharField(max_length=100, null=True ) # the data plans from each network when picked will appear here.
    
    class Meta:
        verbose_name_plural = 'SME DATA'
        

class buy_airtime (models.Model):
    network = models.CharField(max_length=20, choices=NETWORK, null=True )
    phone = models.IntegerField( null=True )
    amount = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Airtime Purchase'
        
        
class sell_to_us(models.Model):
    network = models.CharField(max_length=20, choices=NETWORK, null=True )
    phone = models.IntegerField( null=True )
    amount = models.IntegerField( null=True)
    percent_deducted = models.IntegerField(null=True)
   
    class Meta:
        verbose_name_plural = 'Airtime Sale'
        
         
class bulk_sms(models.Model):
    sender = models.CharField(max_length=100, null=True)
    recipient = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = 'Bulk SMS'
        
        
class cable(models.Model):
    biller = models.CharField(max_length=20, choices = BILLER, null=True)
    payment_item = models.CharField(max_length=20, null=True)
    smartcard_number = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Cable'