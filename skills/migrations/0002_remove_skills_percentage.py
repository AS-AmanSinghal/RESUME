# Generated by Django 4.0.6 on 2022-07-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='percentage',
        ),
    ]
