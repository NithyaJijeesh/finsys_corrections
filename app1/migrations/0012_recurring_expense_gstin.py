# Generated by Django 3.2.14 on 2023-06-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_vendor_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_expense',
            name='gstin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
