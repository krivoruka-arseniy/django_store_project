# Generated by Django 5.1.2 on 2024-10-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(default=1, upload_to='product_imgs'),
            preserve_default=False,
        ),
    ]
