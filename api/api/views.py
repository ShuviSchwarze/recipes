from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.contrib.auth.models import User, Group
from . import serializer
from rest_framework import viewsets, permissions
from . import constants as const


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializer.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
#
#
#class GroupViewSet(viewsets.ModelViewSet):
#    queryset = Group.objects.all()
#    serializer_class = serializer.GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class ProfileViewSet(viewsets.ModelViewSet):
#    queryset = models.Profile.objects.all()
#    serializer_class = serializer.ProfileSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class CuisineViewSet(viewsets.ModelViewSet):
#    queryset = models.Cuisine.objects.all()
#    serializer_class = serializer.CuisineSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class DishTypeViewSet(viewsets.ModelViewSet):
#    queryset = models.DishType.objects.all()
#    serializer_class = serializer.DishTypeSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class AllergenViewSet(viewsets.ModelViewSet):
#    queryset = models.Allergen.objects.all()
#    serializer_class = serializer.AllergenSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class UnitViewSet(viewsets.ModelViewSet):
#    queryset = models.Unit.objects.all()
#    serializer_class = serializer.UnitSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class IngredientViewSet(viewsets.ModelViewSet):
#    queryset = models.Ingredient.objects.all()
#    serializer_class = serializer.IngredientSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class InstructionViewSet(viewsets.ModelViewSet):
#    queryset = models.Instruction.objects.all()
#    serializer_class = serializer.InstructionSerializer
#    permission_classes = [permissions.AllowAny]
#
#
#class RecipeAttachmentViewSet(viewsets.ModelViewSet):
#    queryset = models.RecipeAttachments.objects.all()
#    serializer_class = serializer.RecipeAttachmentSerializer
#    permission_classes = [permissions.IsAuthenticated]
#
#
#class RecipeIngredientViewSet(viewsets.ModelViewSet):
#    queryset = models.RecipeIngredients.objects.all()
#    serializer_class = serializer.RecipeIngredientSerializer
#    permission_classes = [permissions.IsAuthenticated]