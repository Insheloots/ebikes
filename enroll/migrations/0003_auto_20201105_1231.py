# Generated by Django 3.1.3 on 2020-11-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20201105_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio_unit',
            field=models.DecimalField(decimal_places=8, max_digits=11),
        ),
    ]