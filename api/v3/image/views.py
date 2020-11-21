import redis
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView

from api.v3.image.image_processing import compose_imageproxy_response

# Connect to Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class ImageProxy(APIView):
    def get(self, request, *args, **kwargs):
        new_width = kwargs.get('width')
        link = kwargs.get('link')
        key = str(new_width) + link

        value = redis_instance.get(key)
        if value is not None:

            return HttpResponse(value, content_type='image/png')
        else:
            resized_image_bytes = compose_imageproxy_response(new_width, link)
            redis_instance.set(key, resized_image_bytes, ex=3600 * 2)
            return HttpResponse(resized_image_bytes, content_type='image/png')
