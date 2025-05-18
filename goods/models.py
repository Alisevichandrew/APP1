from tabnanny import verbose
from unicodedata import category
from django.core.validators import slug_re
from django.db import models


# Create your models here.
class Categories(models.Model):
    # перечисляем поля и т-цы
    # slug - фрагмент URL адреса, к-рый будет вести на следующую категорию
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    # blank=True, null=True - применяется, если изображения не будет
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0.00, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"
