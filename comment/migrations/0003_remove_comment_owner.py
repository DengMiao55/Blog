# Generated by Django 2.1.8 on 2020-02-18 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200218_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
