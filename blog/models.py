from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    """ Категория услуг """
    name = models.CharField("Название категории", max_length = 120)
    slug = models.SlugField("URL", max_length = 120)
    text = models.TextField("Текст категории")
    banner = models.ImageField("Баннер", upload_to = "image/", blank = True, null = True)
    title = models.CharField("Title", max_length = 250)
    description = models.CharField("Description", max_length = 250)
    keywords = models.CharField("Keywords", max_length = 250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog_category", kwargs = {"slug" : self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Model(models.Model):
    """ Модель из категории"""
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, verbose_name = "Выбор категории" )
    name = models.CharField("Название услуги", max_length = 120)
    slug = models.SlugField("URL", max_length = 120, default = "", unique = True)
    text = models.TextField("Текст модели", default = "")
    header = models.CharField("Заголовок", max_length = 120, blank = True, null = True)
    sub_header = models.CharField("Подзаголовок", max_length = 200, blank = True, null = True)
    images = models.ImageField("Картинка чего-либо", upload_to = "images/", blank = True, null = True)
    active = models.BooleanField("Опубликовать", default = True)
    title = models.CharField("Title", max_length = 120)
    description = models.CharField("Description", max_length = 250)
    keywords = models.CharField("Keywords", max_length = 250)
    sort = models.PositiveIntegerField("Порядок", default = 0, unique = True)
    price = models.CharField("Цена", max_length = 20, default ="")




    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog_service_view", kwargs = {"category" : self.category.slug, "slug" : self.slug})


    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
