# Generated by Django 3.0.2 on 2020-01-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
