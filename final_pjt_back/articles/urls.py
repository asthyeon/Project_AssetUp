from django.urls import path
from . import views

urlpatterns = [
    # 게시판 글 목록 불러오기
    path('board-articles/', views.board_article_list),
    # 게시판 글 상세보기
    path('board-articles/<int:board_article_pk>/', views.board_article_detail),
]
