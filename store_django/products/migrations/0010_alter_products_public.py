# Generated by Django 5.1.2 on 2024-10-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_products_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='public',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
