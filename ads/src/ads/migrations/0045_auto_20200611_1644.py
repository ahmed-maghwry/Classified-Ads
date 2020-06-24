# Generated by Django 2.1.5 on 2020-06-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0044_auto_20200611_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_furnisher',
            name='room_area',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Area (m²) '),
        ),
        migrations.AlterField(
            model_name='db_jops_services',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='db_pets',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]