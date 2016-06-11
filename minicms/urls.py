"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from django_summernote import urls as summernote_urls
from news import views as news_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include(summernote_urls)),
    url(r'^$', news_views.index, name='index'),
    url(r'column/(?P<column_slug>[^/]+)/$', news_views.column_detail, name='column'),
    url(r'news/(?P<article_slug>[^/]+)/$', news_views.article_detail, name='article'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
