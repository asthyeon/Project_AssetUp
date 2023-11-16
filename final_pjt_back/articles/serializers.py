from rest_framework import serializers
from .models import BoardArticle


# 게시판 글 리스트
class BoardArticleListSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BoardArticle
        fields = ('id', 'user_name', 'title', 'content')


# 게시판 글 단일
class BoardArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardArticle
        fields = '__all__'
        read_only_fields = ('user',)