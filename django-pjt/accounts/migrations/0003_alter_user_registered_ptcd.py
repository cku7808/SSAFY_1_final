# Generated by Django 4.2.16 on 2024-11-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_registered_ptcd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registered_ptcd',
            field=models.JSONField(default=list),
        ),
    ]