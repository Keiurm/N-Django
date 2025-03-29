from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("next", views.next, name="next"),
    path("form", views.form, name="form"),
    path("result", views.form_result, name="form_result"),
    path("new_form", views.new_form, name="new_form"),
]
