# Generated by Django 4.0.3 on 2022-03-29 14:14
from django.contrib.postgres.operations import TrigramExtension

import apps.posts.models
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        TrigramExtension(),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_draft', models.BooleanField(default=True, verbose_name='draft')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='description')),
                ('content', models.TextField(verbose_name='content')),
                ('raw_slug', models.CharField(blank=True, max_length=50, verbose_name='raw slug')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, verbose_name='slug')),
                ('hash', models.CharField(default=apps.posts.models.gen_hash, editable=False, max_length=15, unique=True, verbose_name='hash')),
                ('primary_image', models.ImageField(null=True, upload_to=apps.posts.models.post_primary_image_upload_path, verbose_name='primary image')),
                ('tags', models.ManyToManyField(related_name='posts', to='tags.tag', verbose_name='tags')),
                ('likes_count', models.PositiveSmallIntegerField(default=0, verbose_name='likes count')),
                ('comments_count', models.PositiveSmallIntegerField(default=0, verbose_name='comments count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('published_at', models.DateTimeField(null=True, verbose_name='published at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('likes', models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='likes')),
            ],
        ),
    ]
