# Generated by Django 4.2.5 on 2024-02-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("petsapp", "0002_pet_image_alter_pet_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pet",
            old_name="Age",
            new_name="age",
        ),
        migrations.RenameField(
            model_name="pet",
            old_name="Breed",
            new_name="breed",
        ),
        migrations.RenameField(
            model_name="pet",
            old_name="Gender",
            new_name="gender",
        ),
        migrations.RenameField(
            model_name="pet",
            old_name="Name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="pet",
            name="Description",
        ),
        migrations.RemoveField(
            model_name="pet",
            name="Species",
        ),
        migrations.AddField(
            model_name="pet",
            name="animal_type",
            field=models.CharField(
                choices=[("D", "Dog"), ("C", "Cat")], default=1, max_length=30
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pet",
            name="price",
            field=models.FloatField(default="10"),
        ),
        migrations.AddField(
            model_name="pet",
            name="slug",
            field=models.SlugField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="pet",
            name="description",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
