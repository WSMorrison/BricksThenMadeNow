# Generated by Django 3.2.19 on 2023-07-05 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteuser_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('siteuser_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('siteuser_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('siteuser_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('siteuser_state', models.CharField(blank=True, max_length=80, null=True)),
                ('siteuser_zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('siteuser_country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]