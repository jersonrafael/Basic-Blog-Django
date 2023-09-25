# Generated by Django 4.2.5 on 2023-09-16 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_datecreate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postComments',
        ),
        migrations.AlterField(
            model_name='post',
            name='dateCreate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 16, 18, 14, 37, 240394, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
