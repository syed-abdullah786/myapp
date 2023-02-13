# Generated by Django 4.1.2 on 2023-02-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='timeline',
        ),
        migrations.AddField(
            model_name='note',
            name='order',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeline',
            name='order',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.order'),
            preserve_default=False,
        ),
    ]