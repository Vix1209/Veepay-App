# Generated by Django 4.2 on 2023-06-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='person_fill_icon.png', upload_to='static/Profile_Images'),
        ),
    ]