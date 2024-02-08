# Generated by Django 4.2.5 on 2024-02-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("petsapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="image",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name="pet",
            table="Pet",
        ),
    ]
