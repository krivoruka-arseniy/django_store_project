# Generated by Django 5.1.2 on 2024-10-30 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.status'),
        ),
    ]
