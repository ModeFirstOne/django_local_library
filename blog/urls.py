from django.urls import path

from . views import *

urlpatterns = [
    path("", posts_list),
    path("", CategoryList.as_view(), name = "category_list"),
    path("<slug:slug>/", ServiceModel.as_view(), name = "blog_category"),
    path("<slug:category>/<slug:slug>/", ServiceModelView.as_view(), name = "blog_service_view"),
]

#path("", posts_list)
