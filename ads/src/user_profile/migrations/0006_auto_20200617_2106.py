# Generated by Django 2.1.5 on 2020-06-17 19:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0005_user_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_details',
            new_name='adress_details',
        ),
        migrations.RenameField(
            model_name='adress_details',
            old_name='adress_details',
            new_name='adress_description',
        ),
    ]
