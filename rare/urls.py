"""rare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rareapi.views import login_user, register_user, check_admin, RareUserView, PostView, CategoryView, TagView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'users', RareUserView, 'post')
router.register(r'categories', CategoryView, 'category')

router.register(r'tags', TagView, 'tag')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('authorize', check_admin),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]