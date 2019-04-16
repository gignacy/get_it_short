from django.urls import path
from shorten.views import LinkView
from . import views

urlpatterns = [
    path('', LinkView.as_view(), name='index'),
    path('<int:shorten_id>/', LinkView.results, name='results')
]