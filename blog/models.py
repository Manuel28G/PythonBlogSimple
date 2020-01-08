from django.db import models


class Article(models.Model):
    title = models.CharField('Title of article', max_length=300)
    content = models.TextField('Content of article', max_length=2000, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title