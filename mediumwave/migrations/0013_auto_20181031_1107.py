# Generated by Django 2.1.2 on 2018-10-31 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediumwave', '0012_transmitter_country_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
