# Generated by Django 3.2.9 on 2022-01-09 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majiraniapp', '0009_auto_20220109_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='neigcount',
        ),
    ]
