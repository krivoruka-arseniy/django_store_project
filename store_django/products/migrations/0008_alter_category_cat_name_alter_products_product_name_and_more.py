# Generated by Django 5.1.2 on 2024-10-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_name',
            field=models.CharField(max_length=15),
        ),
    ]
