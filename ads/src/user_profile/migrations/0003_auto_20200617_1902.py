# Generated by Django 2.1.5 on 2020-06-17 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0002_auto_20200617_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AlterField(
            model_name='governorate',
            name='center_city',
            field=models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': True, 'governorate_name__isnull': False, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_center_city', to='user_profile.governorate'),
        ),
    ]