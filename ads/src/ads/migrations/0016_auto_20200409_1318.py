# Generated by Django 2.1.5 on 2020-04-09 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0015_auto_20200409_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='ad_catugr',
        ),
        migrations.AddField(
            model_name='ads',
            name='end',
            field=models.ForeignKey(blank=True, limit_choices_to={'main__isnull': False, 'sub__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_end', to='ads.catugry'),
        ),
        migrations.AddField(
            model_name='ads',
            name='main',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': True, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_main', to='ads.catugry'),
        ),
        migrations.AddField(
            model_name='ads',
            name='sub',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': False, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_sub', to='ads.catugry'),
        ),
        migrations.AlterField(
            model_name='catugry',
            name='end',
            field=models.ForeignKey(blank=True, limit_choices_to={'main__isnull': False, 'sub__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_end', to='ads.catugry'),
        ),
        migrations.AlterField(
            model_name='catugry',
            name='main',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': True, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_main', to='ads.catugry'),
        ),
        migrations.AlterField(
            model_name='catugry',
            name='sub',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': False, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_sub', to='ads.catugry'),
        ),
    ]
