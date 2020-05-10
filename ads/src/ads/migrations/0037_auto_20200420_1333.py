# Generated by Django 3.0.4 on 2020-04-20 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0036_auto_20200420_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='end',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': False, 'sub__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_end', to='ads.catugry'),
        ),
    ]