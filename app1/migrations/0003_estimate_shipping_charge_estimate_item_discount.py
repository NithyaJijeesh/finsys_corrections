# Generated by Django 4.1 on 2023-08-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_salescreditnote_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='shipping_charge',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estimate_item',
            name='discount',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]
