from django.urls import path, include

from api.v1.image.views import ImageCreate

urlpatterns = [
    path('image/', ImageCreate.as_view()),
]
