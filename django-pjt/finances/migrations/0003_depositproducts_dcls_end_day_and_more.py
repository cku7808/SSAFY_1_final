# Generated by Django 4.2.16 on 2024-11-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_depositproducts_savingproducts_savingoption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositproducts',
            name='dcls_end_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='depositproducts',
            name='dcls_strt_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='savingproducts',
            name='dcls_end_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='savingproducts',
            name='dcls_strt_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]