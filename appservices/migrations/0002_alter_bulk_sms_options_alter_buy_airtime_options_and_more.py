# Generated by Django 4.2 on 2023-05-03 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appservices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulk_sms',
            options={'verbose_name_plural': 'Bulk SMS'},
        ),
        migrations.AlterModelOptions(
            name='buy_airtime',
            options={'verbose_name_plural': 'Airtime Purchase'},
        ),
        migrations.AlterModelOptions(
            name='cable',
            options={'verbose_name_plural': 'Cable'},
        ),
        migrations.AlterModelOptions(
            name='sell_to_us',
            options={'verbose_name_plural': 'Airtime Sale'},
        ),
        migrations.AlterModelOptions(
            name='sme_data',
            options={'verbose_name_plural': 'SME DATA'},
        ),
    ]
