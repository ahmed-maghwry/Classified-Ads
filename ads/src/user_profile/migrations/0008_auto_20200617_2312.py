# Generated by Django 2.1.5 on 2020-06-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_user_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='favoret_ads',
        ),
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
