# Generated by Django 3.2.5 on 2021-07-10 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0019_auto_20210710_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTotalHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrightSparkEducation', models.IntegerField(default=0)),
                ('Transformers', models.IntegerField(default=0)),
                ('FoodNutrition', models.IntegerField(default=0)),
                ('GenderProgram', models.IntegerField(default=0)),
                ('YoungistaanAnimalHeroes', models.IntegerField(default=0)),
                ('BloodDonor', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='checkeradmin',
            name='task_done',
        ),
        migrations.RemoveField(
            model_name='checkeradmin',
            name='user_using',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='CheckerAdmin',
        ),
    ]
