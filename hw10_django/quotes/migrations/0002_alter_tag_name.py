# Generated by Django 4.2.6 on 2023-10-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
