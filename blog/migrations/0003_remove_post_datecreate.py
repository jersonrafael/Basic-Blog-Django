# Generated by Django 4.2.5 on 2023-09-13 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_datecreate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dateCreate',
        ),
    ]
