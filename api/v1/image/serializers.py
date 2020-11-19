import os
import time
from io import BytesIO

import requests
from PIL import Image as Im
from django.conf import settings
from rest_framework import serializers

from image.models import Image


class ImageUploadSerializer(serializers.Serializer):
    url = serializers.URLField(write_only=True)
    width = serializers.IntegerField(write_only=True)
    saved_image = serializers.URLField(read_only=True)

    def create(self, validated_data):
        url = validated_data['url']
        width = validated_data['width']

        response = requests.get(url)

        img = Im.open(BytesIO(response.content))
        source_width = img.width
        source_height = img.height
        k = source_width / width
        height = int(source_height / k)

        resized_img = img.resize((width, height))
        img_name = str(time.time()) + '.jpg'
        path = os.path.join(settings.MEDIA_ROOT, img_name)
        resized_img.save(path)
        instance = Image(saved_image=path)
        instance.save()

        return instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['saved_image']
