from rest_framework import serializers
from .models import Article, Comment


# 게시판 글 리스트
class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ('id', 'username', 'title', 'content')


# 게시판 댓글 조회 
class CommentSerializer(serializers.ModelSerializer):
    # override
    article = ArticleListSerializer(read_only=True)
    username = serializers.ReadOnlyField(source='author.username') 


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)


# 게시판 글 단일
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author', 'like_authors')