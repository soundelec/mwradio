# Generated by Django 2.1.2 on 2018-10-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumwave', '0005_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(default='bar', max_length=512),
            preserve_default=False,
        ),
    ]