# Generated by Django 5.2 on 2025-04-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_watering_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watering',
            name='amount',
            field=models.CharField(choices=[('Cup', '8oz'), ('Pitcher', '32oz'), ('Watering Can', '64oz')], default='Cup', max_length=25),
        ),
    ]
