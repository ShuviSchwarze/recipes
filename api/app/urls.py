"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers
import api.views as views


from upload.views import image_upload

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"profiles", views.ProfileViewSet)
router.register(r"cuisines", views.CuisineViewSet)
router.register(r"dish_types", views.DishTypeViewSet)
router.register(r"allegens", views.AllergenViewSet)
router.register(r"units", views.UnitViewSet)
router.register(r"ingredients", views.IngredientViewSet)
router.register(r"recipes", views.RecipeViewSet)
router.register(r"instructions", views.InstructionViewSet)
router.register(r"recipe_attachments", views.RecipeAttachmentViewSet)
router.register(r"recipe_ingredients", views.RecipeIngredientViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("upload/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
