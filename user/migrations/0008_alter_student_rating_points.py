# Generated by Django 4.2.5 on 2023-10-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_student_absence_day_student_injury_day_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="rating_points",
            field=models.IntegerField(default=0),
        ),
    ]
