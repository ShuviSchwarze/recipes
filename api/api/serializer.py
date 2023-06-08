from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = ["user", "avatar", "json_information"]


class CuisineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cuisine
        fields = ["name"]


class DishTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DishType
        fields = ["name"]


class AllergenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Allergen
        fields = ["name"]


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Unit
        fields = ["name", "type", "system", "base_value"]


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = [
            "name",
            "fdc_id",
            "unit",
            "unit_density",
            "base_quantity",
            "description",
            "image",
        ]


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Recipe
        fields = [
            "url",
            "author",
            "cuisine",
            "dish_type",
            "title",
            "summary",
            "status",
            "cooking_time",
            "nutritonal_values",
            "difficulty",
            "created_at",
            "updated_at",
        ]


class InstructionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Instruction
        fields = [
            "url",
            "recipe",
            "step_number",
            "media",
        ]


class RecipeAttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RecipeAttachments
        fields = [
            "url",
            "recipe",
            "title",
        ]


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RecipeIngredients
        fields = [
            "recipe",
            "ingredient",
            "quantity",
            "unit",
        ]
