from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView, PaginatedArticleListAPIView, blog_list_view

urlpatterns = [
    # API endpoints
    path('articles/', ArticleListAPIView.as_view(), name='article-list'),
    path('articles/paginated/', PaginatedArticleListAPIView.as_view(), name='paginated-article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),

    # Template view
    path('blog/', blog_list_view, name='blog-list'),
]
