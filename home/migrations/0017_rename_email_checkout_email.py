# Generated by Django 4.2.5 on 2023-10-21 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_checkout_ship_remove_checkout_shipaddress_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='Email',
            new_name='email',
        ),
    ]
