# Generated by Django 3.2.19 on 2023-06-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20230629_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]