# Generated by Django 4.2.16 on 2024-11-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todaycurrency',
            name='img',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
