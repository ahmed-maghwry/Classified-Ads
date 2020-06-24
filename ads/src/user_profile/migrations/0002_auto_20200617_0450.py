# Generated by Django 2.1.5 on 2020-06-17 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='governorate',
            options={'verbose_name': 'governorate', 'verbose_name_plural': 'governorate'},
        ),
        migrations.AddField(
            model_name='governorate',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='governorate',
            name='region_village',
            field=models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': False, 'governorate_name__isnull': False, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_region_village', to='user_profile.governorate'),
        ),
        migrations.AlterField(
            model_name='governorate',
            name='center_city',
            field=models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': False, 'governorate_name__isnull': True, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_center_city', to='user_profile.governorate'),
        ),
        migrations.AlterField(
            model_name='governorate',
            name='governorate_name',
            field=models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': True, 'governorate_name__isnull': True, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_governorate_name', to='user_profile.governorate'),
        ),
    ]