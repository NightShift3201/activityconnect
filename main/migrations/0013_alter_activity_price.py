# Generated by Django 4.1.4 on 2023-01-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_activity_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
