# Generated by Django 5.0 on 2023-12-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.DateTimeField(),
        ),
    ]