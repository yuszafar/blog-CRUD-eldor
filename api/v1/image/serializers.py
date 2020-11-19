from rest_framework import serializers

from image.models import Image


class ImageSerializer(serializers.Serializer):

    class Meta:
        fields = ('saved_image',)
        model = Image


