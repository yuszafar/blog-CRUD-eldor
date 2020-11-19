from io import BytesIO

from rest_framework import serializers

from image.models import Image

import PIL
import requests


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    width = serializers.IntegerField()

    class Meta:
        fields = ('saved_image', 'url', 'width')
        read_only_fields = ('saved_image',)
        model = Image

    def create(self, validated_data):
        url = validated_data['url']
        width = validated_data['width']

        response = requests.get(url)

        img = PIL.Image.open(BytesIO(response.content))
        source_width = img.width
        source_height = img.height
        k = source_width / width
        height = int(source_height * k)

        resized_img = img.resize((width, height))

        instance = Image(saved_image=resized_img)
        return instance
