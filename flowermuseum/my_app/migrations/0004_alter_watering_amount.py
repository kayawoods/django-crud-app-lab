# Generated by Django 5.2 on 2025-04-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_watering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watering',
            name='amount',
            field=models.CharField(default='Cup', max_length=10),
        ),
    ]
