# Generated by Django 5.0.8 on 2024-08-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_alter_habit_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.DateTimeField(verbose_name="Дата и время привычки"),
        ),
    ]
