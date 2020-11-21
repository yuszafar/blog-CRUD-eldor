from django.urls import path, include

from api.v3.image.views import ImageProxy

urlpatterns = [
    path('imageproxy/<int:width>/<path:link>/', ImageProxy.as_view()),
]
