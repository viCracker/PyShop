# Generated by Django 5.0.4 on 2024-04-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("code", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("discount", models.FloatField()),
            ],
        ),
    ]
