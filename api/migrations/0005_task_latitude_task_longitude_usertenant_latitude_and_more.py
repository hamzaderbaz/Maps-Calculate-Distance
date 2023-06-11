# Generated by Django 4.2 on 2023-06-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_task_latitude_remove_task_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertenant',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertenant',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
