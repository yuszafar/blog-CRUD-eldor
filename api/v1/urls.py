from django.urls import path, include

from api.v1.image.views import ImageCreate, ImageList

urlpatterns = [
    path('image/', ImageCreate.as_view()),
    path('image/list/', ImageList.as_view()),
]
