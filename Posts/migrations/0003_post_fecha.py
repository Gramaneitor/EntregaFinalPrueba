# Generated by Django 4.0.4 on 2022-04-30 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_remove_post_fecha_remove_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
