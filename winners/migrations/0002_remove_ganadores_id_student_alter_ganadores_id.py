# Generated by Django 4.2.7 on 2023-11-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("winners", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ganadores",
            name="id_student",
        ),
        migrations.AlterField(
            model_name="ganadores",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]