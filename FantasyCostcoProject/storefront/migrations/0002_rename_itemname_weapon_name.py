# Generated by Django 4.0.1 on 2022-01-27 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='itemname',
            new_name='name',
        ),
    ]
