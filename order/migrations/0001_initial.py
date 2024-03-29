# Generated by Django 4.2.5 on 2024-02-06 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("petsapp", "0003_rename_age_pet_age_rename_breed_pet_breed_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("payment_id", models.CharField(max_length=150)),
                ("amount_paid", models.CharField(max_length=150)),
                ("status", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("order_number", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AP", "Andhra Pradesh"),
                            ("AR", "Arunchal Pradesh"),
                            ("AS", "Assam"),
                            ("BR", "Bihar"),
                            ("CG", "Chhattisgarh"),
                            ("GA", "Goa"),
                            ("GJ", "Gujrat"),
                            ("HR", "Haryana"),
                            ("HP", "Himanchal Prdesh"),
                            ("MP", "Madhya Pradesh"),
                            ("MH", "Maharashtra"),
                            ("MZ", "Mizoram"),
                            ("NL", "Nagaland"),
                            ("OD", "Odisha"),
                            ("PB", "Punjab"),
                        ],
                        default="MH",
                        max_length=100,
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("total", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "new"),
                            ("pending", "pending"),
                            ("delivered", "delivered"),
                            ("cancelled", "cancelled"),
                        ],
                        default="new",
                        max_length=100,
                    ),
                ),
                ("ip", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "payment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="order.payment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderPet",
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
                ("quantity", models.IntegerField()),
                ("pet_price", models.FloatField()),
                ("is_orderd", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "payment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="order.payment",
                    ),
                ),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="petsapp.pet"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
