# Generated by Django 4.2.5 on 2023-10-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0009_alter_student_belt_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="student_avatars/"
            ),
        ),
    ]
