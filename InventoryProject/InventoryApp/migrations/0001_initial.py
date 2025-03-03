# Generated by Django 5.0.7 on 2024-07-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(max_length=100)),
            ],
        ),
    ]
