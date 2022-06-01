
#
from django.urls import path

from . import views

app_name = "Ajax_app"

urlpatterns = [
    path(
        '',
        views.SuscriptorCreateView.as_view(),
        name='suscriptor-add'
    ),
]