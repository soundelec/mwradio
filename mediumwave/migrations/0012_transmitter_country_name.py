# Generated by Django 2.1.2 on 2018-10-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumwave', '0011_transmitter_iso'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmitter',
            name='country_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
