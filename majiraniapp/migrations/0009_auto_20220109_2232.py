# Generated by Django 3.2.9 on 2022-01-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majiraniapp', '0008_remove_occupant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='neigcount',
            field=models.IntegerField(),
        ),
    ]
