# Generated by Django 4.2.16 on 2024-11-09 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0004_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["completed", "-created_at"]},
        ),
    ]
