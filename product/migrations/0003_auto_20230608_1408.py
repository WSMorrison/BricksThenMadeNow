# Generated by Django 3.2.19 on 2023-06-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_item_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_detail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_modern',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_old',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_render',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
