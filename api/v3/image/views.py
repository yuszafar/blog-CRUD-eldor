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

        timeout = 3600 * 2

        value = redis_instance.get(key)
        if value is None:
            response_content = compose_imageproxy_response(new_width, link)
            redis_instance.set(key, response_content, ex=timeout)
        else:
            redis_instance.expire(key, time=timeout)
            response_content = value

        return HttpResponse(response_content, content_type='image/png')
