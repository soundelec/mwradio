# Generated by Django 2.1.2 on 2018-11-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumwave', '0013_auto_20181031_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='subnetwork',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
