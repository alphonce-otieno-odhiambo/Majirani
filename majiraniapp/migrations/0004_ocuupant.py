# Generated by Django 3.2.9 on 2022-01-09 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majiraniapp', '0003_neighborhood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocuupant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neigborhood', to='majiraniapp.neighborhood')),
            ],
        ),
    ]