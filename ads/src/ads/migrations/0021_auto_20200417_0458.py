# Generated by Django 3.0.4 on 2020-04-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0020_auto_20200416_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='catugry',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
