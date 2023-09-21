# Generated by Django 4.2.5 on 2023-09-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(),
        ),
    ]
