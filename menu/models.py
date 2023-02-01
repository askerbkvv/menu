from django.db import models


class Category(models.Model):
    name = models.CharField("Тип Продукта", max_length=100, blank=True, null=True)
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Menu(models.Model):
    menu = models.CharField("Меню", max_length=100, blank=True, null=True)
    url = models.CharField('Ссылка', max_length=255)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.menu

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Menu")


class Products(models.Model):
    title = models.CharField("Наименование", max_length=100, blank=True, null=True)
    content = models.TextField("Описание", max_length=250, blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Food")
        verbose_name_plural = ("Food")











