# Generated by Django 4.1.4 on 2023-01-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_day_activity_days_of_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activityPage',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='city',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='activity',
            name='country',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='activity',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=25),
        ),
        migrations.AddField(
            model_name='activity',
            name='hostName',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='activity',
            name='maxAge',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='activity',
            name='minAge',
            field=models.IntegerField(blank=True, default=5),
        ),
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.IntegerField(blank=True, default=5),
        ),
        migrations.AddField(
            model_name='activity',
            name='state',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='activity',
            name='streetAddress',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]