from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView,
    LikeForArticle,
    UnlikeForArticle,
    UnlikeForComment,
    LikeForComment
)


app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/like_comment', LikeForComment.as_view(),   name='like_comment'),
    path('<int:pk>/unlike_comment', UnlikeForComment.as_view(),  name='unlike_comment'),
    path('<int:pk>/like_article', LikeForArticle.as_view(),  name='like_article'),
    path('<int:pk>/unlike_article', UnlikeForArticle.as_view(),  name='unlike_article'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
]
