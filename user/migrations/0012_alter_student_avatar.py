# Generated by Django 4.2.5 on 2023-10-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0011_alter_student_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="avatar",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
