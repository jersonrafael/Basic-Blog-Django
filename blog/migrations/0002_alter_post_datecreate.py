# Generated by Django 4.2.5 on 2023-09-13 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreate',
            field=models.DateField(verbose_name=datetime.datetime.now),
        ),
    ]
