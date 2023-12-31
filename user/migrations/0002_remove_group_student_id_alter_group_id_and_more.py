# Generated by Django 4.2.5 on 2023-09-19 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="student_id",
        ),
        migrations.AlterField(
            model_name="group",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="GroupsAndStudents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.group"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.student"
                    ),
                ),
            ],
        ),
    ]
