# Generated by Django 4.0.2 on 2022-02-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_condition_alter_car_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
