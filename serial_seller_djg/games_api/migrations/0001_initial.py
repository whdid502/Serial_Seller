# Generated by Django 3.0.4 on 2020-04-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=30)),
                ('link', models.TextField()),
                ('img', models.TextField()),
                ('title', models.CharField(max_length=30)),
                ('original_price', models.IntegerField()),
                ('discount_rate', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('original_price_usd', models.IntegerField()),
                ('discount_price_usd', models.IntegerField()),
            ],
        ),
    ]
