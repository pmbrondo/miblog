# Generated by Django 4.2.6 on 2024-01-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]