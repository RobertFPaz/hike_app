# Generated by Django 2.2 on 2021-07-12 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0008_auto_20210712_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]