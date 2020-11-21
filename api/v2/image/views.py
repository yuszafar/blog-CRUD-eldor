from django.http import HttpResponse
from rest_framework.views import APIView

from api.v2.image.image_processing import compose_imageproxy_response


class ImageProxy(APIView):
    def get(self, request, *args, **kwargs):
        new_width = kwargs.get('width')
        link = kwargs.get('link')
        resized_image_bytes = compose_imageproxy_response(new_width, link)
        return HttpResponse(resized_image_bytes, content_type='image/png')
