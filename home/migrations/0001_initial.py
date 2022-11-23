# Generated by Django 4.1.3 on 2022-11-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Layoffs", "Layoffs"),
                            ("HIRING FREEZE", "Hiring Freeze"),
                            ("Hiring", "Hiring"),
                        ],
                        default="Hiring",
                        max_length=50,
                    ),
                ),
                ("last_update", models.DateTimeField(auto_now_add=True)),
                ("application_link", models.URLField(blank=True)),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]