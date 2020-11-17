from rest_framework import serializers
from .models import Post, Commentary, User
from rest_framework.fields import CurrentUserDefault


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('id', 'author', 'title', 'body')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('id', 'post', 'body', 'author')
        model = Commentary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

