from django.urls import path
from api.views import MovieView

urlpatterns = [
    path('movie', MovieView.as_view(), name='movie'),
]