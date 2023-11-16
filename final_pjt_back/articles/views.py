from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import BoardArticle
from .serializers import BoardArticleListSerializer, BoardArticleSerializer

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# 게시판 글 전체 대상
@api_view(['GET', 'POST'])
def board_article_list(request):
    # 게시판 글 전체 조회
    if request.method == 'GET':
        board_articles = get_list_or_404(BoardArticle)
        serializer = BoardArticleListSerializer(board_articles, many=True)
        return Response(serializer.data)
    
    # 게시판 글 작성
    elif request.method == 'POST':
        serializer = BoardArticleSerializer(data=request.data)
        if serializer.is_vaild(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시판 단일 게시글 대상
@api_view(['GET', 'DELETE', 'PUT'])
def board_article_detail(request, board_article_pk):
    board_article = get_object_or_404(BoardArticle, pk=board_article_pk)

    # 게시판 단일 게시글 조회
    if request.method == 'GET':
        serializer = BoardArticleSerializer(board_article)
        return Response(serializer.data)
    
    # 게시판 단일 게시글 삭제
    elif request.method == 'DELETE':
        board_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 게시판 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = BoardArticleSerializer(board_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)