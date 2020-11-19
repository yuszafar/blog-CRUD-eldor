from rest_framework.generics import CreateAPIView, ListAPIView

from api.v1.image.serializers import ImageUploadSerializer, ImageSerializer
from image.models import Image


class ImageCreate(CreateAPIView):
    serializer_class = ImageUploadSerializer


class ImageList(ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
