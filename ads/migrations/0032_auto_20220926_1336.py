# Generated by Django 3.2.13 on 2022-09-26 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0031_alter_ads_condition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='condition',
            new_name='entry',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='price',
            new_name='prize',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='brand',
            new_name='registeration_url',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='state',
        ),
        migrations.AddField(
            model_name='ads',
            name='regsiteration_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]