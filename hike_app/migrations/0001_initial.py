# Generated by Django 2.2 on 2021-07-12 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0008_auto_20210712_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('max_attendees', models.IntegerField()),
                ('difficulty', models.CharField(max_length=60)),
                ('pets', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attend', models.ManyToManyField(related_name='user_hikes', to='login_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hikes', to='login_app.User')),
            ],
        ),
    ]
