from rest_framework import serializers
from blog.models import Article
"""
Serializer to articles
"""


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        """
        Al colocar all se configura para que se haga la serialización de todos los campos
        para serializar solo el titulo se colocaría
        fields = ('title')
        """
        fields = '__all__'
