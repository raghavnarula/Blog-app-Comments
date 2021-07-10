# Generated by Django 3.2.5 on 2021-07-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BrightSparkEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodNutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GenderProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transformers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='YoungistaanAnimalHeroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='None', max_length=50)),
                ('Total_hours_done', models.IntegerField(default=0)),
            ],
        ),
    ]