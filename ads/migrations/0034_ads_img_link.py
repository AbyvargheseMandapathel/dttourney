# Generated by Django 3.2.13 on 2022-10-05 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0033_rename_regsiteration_url_ads_no_of_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
