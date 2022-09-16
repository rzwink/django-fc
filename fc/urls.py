"""fc URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include
from django.urls import path


def redirect_view(request):
    if request.user.is_authenticated:
        response = redirect("/web/")
    else:
        response = redirect("/web/")
    return response


urlpatterns = [
    path("", redirect_view),
    path("admin/", admin.site.urls),
    path("web/", include("web.urls")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
