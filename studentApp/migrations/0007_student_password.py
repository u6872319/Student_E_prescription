# Generated by Django 3.1 on 2021-05-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0006_auto_20210508_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
