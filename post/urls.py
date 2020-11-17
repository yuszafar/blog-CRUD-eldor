from django.urls import path
from .views import PostList, PostDetail, PostCreate, CommentaryCreate, CommentaryList, CommentDetail, UserCreate


urlpatterns = [
    path('post/<int:pk>/', PostDetail.as_view()),
    path('post/list/', PostList.as_view()),
    path('post/create', PostCreate.as_view()),
    path('commentary/create', CommentaryCreate.as_view()),
    path('commentary/list', CommentaryList.as_view()),
    path('commentary/<int:pk>/', CommentDetail.as_view()),
    path('account/register', UserCreate.as_view())
]
