# Generated by Django 2.1.7 on 2019-03-08 11:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20190307_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, unique=True),
        ),
    ]