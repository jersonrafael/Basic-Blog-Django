# Generated by Django 4.2.5 on 2023-09-14 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_datecreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentTittle', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='dateCreate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 15, 17, 12, 156554, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='postComment',
            field=models.ManyToManyField(to='blog.comments'),
        ),
    ]
