# Generated by Django 2.0.1 on 2018-02-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180219_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
        ),
    ]
