# Generated by Django 3.0.2 on 2020-01-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title of article')),
                ('content', models.TextField(blank=True, max_length=2000, verbose_name='Content of article')),
            ],
        ),
    ]
