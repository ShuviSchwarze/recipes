# Generated by Django 4.2.1 on 2023-06-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit_density',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
