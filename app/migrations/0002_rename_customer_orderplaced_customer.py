# Generated by Django 3.2.8 on 2021-12-15 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Customer',
            new_name='customer',
        ),
    ]