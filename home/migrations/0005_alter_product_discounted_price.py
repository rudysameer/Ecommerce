# Generated by Django 4.2.5 on 2023-09-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_image_alter_product_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(blank=True),
        ),
    ]
