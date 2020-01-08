from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets , permissions
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title',)
