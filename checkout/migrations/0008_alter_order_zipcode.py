# Generated by Django 3.2.19 on 2023-07-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_siteuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
