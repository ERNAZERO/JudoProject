# Generated by Django 4.2.5 on 2023-09-23 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_belt_alter_student_belt_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="belt_status",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="user.belt"
            ),
        ),
    ]