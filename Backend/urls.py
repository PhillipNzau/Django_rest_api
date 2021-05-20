"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# from blogAPI import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     # path('car', views.add_car),
#     path('<str:car_name>', views.get_car),
# ]
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from Backend import settings
from blogAPI import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'cars', views.CarViewSet)
# router.register(r'blogs', views.BlogViewSet)
# router.register(r'categories', views.CategoryViewSet)
# router.register(r'snippet', views.snippet_list)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
                  # path('', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('snippets/', views.snippet_list),
                  path('blogs/', views.blog_list),
                  path('snippets/<int:pk>', views.snippet_detail),
                  # path('<str:car_name>', views.get_car)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
