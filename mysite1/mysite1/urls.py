"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from mysite1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # http://127.0.0.1:8000/birthday/year(4)/mon(2)/day(2)
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$', views.birthday),
    # http://127.0.0.1:8000/birthday/mon(2)/day(2)/year(4)
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$', views.birthday),
    # http://127.0.0.1:8000/page/1-100
    path('page/<int:page>', views.page_n),
    # templates
    path('test_html/', views.test_html),
    path('test_html_param', views.test_html_param),
    path('test_if_for', views.test_if_for),
    path('mycal', views.test_mycal),

    path('test_static', views.test_static),

    path('music/', include('music.urls')),
    path('sport/', include('sport.urls')),
    path('news/', include('news.urls')),
    path('otm/', include('otm.urls')),
    path('bookstore/', include('bookstore.urls')),
    path('set_cookie', views.set_cookie),
    path('get_cookie', views.get_cookie),
    path('set_session', views.set_session),
    path('get_session', views.get_session),

]
