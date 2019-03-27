"""day19_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path,include

# http://127.0.0.1:8000/cmdb/index/
# http://127.0.0.1:8000/cmdb/login/
# http://127.0.0.1:8000/monitor/index/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cmdb/', include('app01.urls')),
    path('monitor/', include('app02.urls')),
]



# from app01 import  views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', views.index),
#     path('login/', views.login),
#     # path('home/', views.home),  # CBV
#     path('home/', views.Home.as_view()), # FBV
#     # path('detail/', views.detail),
#     re_path('detail-(\d+).html', views.detail),
#     # re_path('detail-(\d+)-(\d+).html', views.detail),
#     # re_path('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
#     re_path('detail-(?P<nid>\d+).html', views.detail),
# ]