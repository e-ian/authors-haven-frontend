from django.urls import path

from authors.apps.articles.views import (
    ArticleListCreate,
    ArticleRetrieveUpdateDestroy,
    RateArticleView,
    TagsView
)

urlpatterns = [
    path(
        'articles/',
        ArticleListCreate.as_view(),
        name='articles'
    ),
    path(
        'articles/<str:slug>/',
        ArticleRetrieveUpdateDestroy.as_view(),
        name='crud-article'
    ),
    path(
        'articles/<str:slug>/rate/',
        RateArticleView.as_view(),
        name='rate-article'
    ),
    path(
        'tags/',
        TagsView.as_view(),
        name='tags'
    )
]
