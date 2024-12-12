# Generated by Django 5.1.2 on 2024-10-30 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_public'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-product_create_time']},
        ),
        migrations.AddIndex(
            model_name='products',
            index=models.Index(fields=['-product_create_time'], name='products_pr_product_3422f2_idx'),
        ),
    ]