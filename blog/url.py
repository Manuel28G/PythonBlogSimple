from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from blog.views import ArticleView

router = DefaultRouter()

router.register(r'articles', ArticleView)
