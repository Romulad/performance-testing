from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


class ArticleListAPIView(generics.ListAPIView):
    """
    API view to retrieve all 100 articles (no pagination)
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'total_articles': queryset.count(),
            'articles': serializer.data
        })


class ArticleDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single article by ID
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PaginatedArticleListAPIView(generics.ListAPIView):
    """
    API view with pagination support for articles
    Uses DRF's built-in pagination to fetch only the requested page from database
    """
    queryset = Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        # Let DRF handle pagination automatically - this fetches only the requested page
        response = super().list(request, *args, **kwargs)

        # Add total count to the response data (separate COUNT query)
        queryset = self.get_queryset()
        if hasattr(response, 'data') and isinstance(response.data, dict):
            response.data['total_articles'] = queryset.count()

        return response


def blog_list_view(request):
    """
    Django template view to render all 100 blog posts as HTML
    """
    articles = Article.objects.all().order_by('-date')

    context = {
        'articles': articles,
        'total_count': articles.count(),
        'page_title': 'All Blog Posts'
    }

    return render(request, 'blog/blog_list.html', context)
