# Generated by Django 3.2.5 on 2021-07-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_formsubmit_total_hours_spent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkeradmin',
            name='upload',
        ),
        migrations.AddField(
            model_name='formsubmit',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
