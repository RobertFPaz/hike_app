# Generated by Django 2.2 on 2021-07-12 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_auto_20210626_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.date(2021, 7, 12)),
        ),
    ]
