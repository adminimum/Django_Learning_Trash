"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path,include
from django.views.generic import TemplateView
from hello import views

product_patterns = [
    path("",views.products),
    path("comments",views.comments),
    path("questions", views.questions)
]

urlpatterns = [
    path("index_form", views.index_form),
    path("index_bd", views.index_bd),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path("index_bd_multi", views.index_bd_multi),
    path("index_stud", views.index_stud),
    path("create_stud/", views.create_stud),
    path("create_prod/", views.create_prod),
    path("edit_prod/<int:id>/", views.edit_prod),
    path("delete_prod/<int:id>/", views.delete_prod),
    path("index_post", views.index_post),
    path("postuser/", views.postuser),
    path("super_contacts",views.super_contacts),
    path("index2",views.index2),
    path("index3",views.index3),
    path("about1", TemplateView.as_view(template_name="about.html",
    extra_context = {"owner":"Maxius company"})),
    path("contacts", TemplateView.as_view(template_name="contacts.html")),
    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about,kwargs={"name":"Tom", "age": 38}),
    re_path(r'^index', views.index),
    re_path(r'^error', views.error400),
    re_path(r'^user/',views.user),
    path('user/<str:name>/<int:age>',views.user),
    re_path(r"^user2/(?P<name>\D+)/(?P<age>\d+)", views.user),
    path("products/<int:id>",include(product_patterns)),
    path("user_with_params", views.user_params),
    path('redirect', views.redirect),
    path('perm_redirect', views.per_redirect),
    path('access', views.access)
]