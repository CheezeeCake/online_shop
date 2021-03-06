# Generated by Django 4.0 on 2021-12-18 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Smartphone",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Наименование"),
                ),
                ("slug", models.SlugField(unique=True)),
                ("image", models.ImageField(upload_to="", verbose_name="Изображение")),
                ("description", models.TextField(null=True, verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Цена"
                    ),
                ),
                (
                    "diagonal",
                    models.CharField(max_length=255, verbose_name="Диагональ"),
                ),
                (
                    "display_type",
                    models.CharField(max_length=255, verbose_name="Тип дисплея"),
                ),
                (
                    "resolution",
                    models.CharField(max_length=255, verbose_name="Разрешение экрана"),
                ),
                (
                    "accum_volume",
                    models.CharField(max_length=255, verbose_name="Объем батареи"),
                ),
                (
                    "ram",
                    models.CharField(max_length=255, verbose_name="Оперативаня память"),
                ),
                (
                    "sd_volume",
                    models.CharField(max_length=255, verbose_name="Объем памяти"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Notebook",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Наименование"),
                ),
                ("slug", models.SlugField(unique=True)),
                ("image", models.ImageField(upload_to="", verbose_name="Изображение")),
                ("description", models.TextField(null=True, verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Цена"
                    ),
                ),
                (
                    "diagonal",
                    models.CharField(max_length=255, verbose_name="Диагональ"),
                ),
                (
                    "display_type",
                    models.CharField(max_length=255, verbose_name="Тип дисплея"),
                ),
                (
                    "processor_freq",
                    models.CharField(max_length=255, verbose_name="Процесссор"),
                ),
                (
                    "ram",
                    models.CharField(max_length=255, verbose_name="Оперативаня память"),
                ),
                ("video", models.CharField(max_length=255, verbose_name="Видеокарта")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
