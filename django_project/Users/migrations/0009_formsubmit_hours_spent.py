# Generated by Django 3.2.5 on 2021-07-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20210710_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmit',
            name='hours_spent',
            field=models.IntegerField(default=0),
        ),
    ]
