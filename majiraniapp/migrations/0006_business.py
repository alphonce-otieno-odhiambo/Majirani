# Generated by Django 3.2.9 on 2022-01-09 22:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('majiraniapp', '0005_auto_20220109_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('bizz_name', models.CharField(max_length=50)),
                ('bizz_id', models.AutoField(primary_key=True, serialize=False)),
                ('bizz_email', models.CharField(max_length=50)),
                ('bizz_neighborhood', models.ManyToManyField(to='majiraniapp.Neighborhood')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
