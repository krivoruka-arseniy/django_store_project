# Generated by Django 5.1.2 on 2024-10-30 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_status_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_status',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.status'),
        ),
    ]
