# Generated by Django 3.2.19 on 2023-05-31 11:05

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=7, unique=True)),
                ('item_name', models.CharField(max_length=40)),
                ('item_description', models.TextField(max_length=250)),
                ('item_old', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_old_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('item_render', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_render_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('item_modern', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_modern_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('item_detail', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_detail_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('item_part_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_number', models.CharField(max_length=5)),
                ('sku_type', models.CharField(choices=[('inst', 'Instructions Only'), ('mdst', 'Modern Set with Bricks'), ('flst', 'Full Set with Modern Set and Vintage Set Bricks')], default='inst', max_length=4)),
                ('sku_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku_physical', models.BooleanField(default=False)),
                ('sku_inventory', models.IntegerField(validators=[product.models.validate_inventory])),
                ('sku_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.theme'),
        ),
    ]
