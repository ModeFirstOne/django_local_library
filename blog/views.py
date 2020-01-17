from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Model
from django.views.generic import ListView, DetailView


# Create your views here.
def posts_list(request):
    return render(request, "blog\index.html")

class CategoryList(ListView):
    """ Список услуг по категории"""
    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = "index.html"

class ServiceModel(ListView):
    """Список услуг по категориям """
    model = Model
    context_object_name = "blog_category"
    template_name = "blog/blog_category.html"

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get("slug"))

class ServiceModelView(DetailView):
    """ Отображение услуги из категорий """
    model = Model
    context_object_name = "blog_model_view"
    template_name = "blog/blog_model.html"

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get("category"), slug = self.kwargs.get("slug"))
