from django.contrib.auth.models import User, Group
from ...models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
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