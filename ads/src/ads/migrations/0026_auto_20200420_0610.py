# Generated by Django 3.0.4 on 2020-04-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0025_auto_20200420_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_form',
            name='abs',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='air_conditioning',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='airbags',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='alarm_System',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='aux_qudio_in',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='bluetooth_system',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='cruise_control',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='edb',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='fog_lights',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='keyless_start',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='leather_seats',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='navigation_system',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='off_Road_tyres',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='parkings_ensors',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='power_locks',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='power_mirrors',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='power_seats',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='power_steering',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='power_windows',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='premium_wheels_rims',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='radio',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='rear_view_camera',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='roof_rack',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='sunroof',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='touch_screen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='transmission_type',
            field=models.CharField(blank=True, choices=[(1, 'Automatic'), (2, 'Manual')], default='Manual', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='car_form',
            name='usb_charger',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='Kilometers',
            field=models.CharField(blank=True, choices=[(1, '0 - 999'), (2, '1000 - 29999 '), (3, '30000 - 49999'), (4, '50000 - 99999'), (5, '100000 - 149999'), (5, '150000 - 199999'), (6, 'More Than 200000')], default='0 - 999', max_length=1, null=True),
        ),
    ]