# Generated by Django 4.1.2 on 2023-01-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customers_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='zip_code',
        ),
    ]