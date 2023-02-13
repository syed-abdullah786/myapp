# Generated by Django 4.1.2 on 2023-02-08 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_address_customer_street_customer_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sku', models.IntegerField()),
                ('buying_price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.customer'),
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(max_length=70)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.customer')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, related_name='notes', to='store.note'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='timeline',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, related_name='timelines', to='store.timeline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(related_name='products', to='store.supplier'),
        ),
    ]
