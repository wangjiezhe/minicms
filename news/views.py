# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from news.models import Column, Article


def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns': columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})

def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'news/article.html', {'article': article})
