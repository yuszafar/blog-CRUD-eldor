from rest_framework import generics
from .models import Post, Commentary, User
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentaryCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Commentary.objects.all()


class CommentaryList(generics.ListAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
