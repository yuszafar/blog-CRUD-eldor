from rest_framework.generics import CreateAPIView

from api.v1.image.serializers import ImageSerializer


class ImageCreate(CreateAPIView):
    serializer_class = ImageSerializer
