from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import constants


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(max_length=255, blank=True, null=True)

    def json_default():
        return {
            "phone_number": "",
            "home_address": {
                "address": "",
                "city": "",
                "state": "",
                "country": "",
                "postal_code": "",
            },
            "billing_address": {
                "address": "",
                "city": "",
                "state": "",
                "country": "",
                "postal_code": "",
            },
            "bank_account_number": "",
        }

    json_information = models.JSONField("jsonInformation", default=json_default)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Cuisine(models.Model):
    name = models.CharField(max_length=50)


class DishType(models.Model):
    name = models.CharField(max_length=50)


class Allergen(models.Model):
    name = models.CharField(max_length=50)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=2,
        choices=constants.UnitType.choices,
        default=constants.UnitType.MASS,
    )
    system = models.CharField(
        max_length=2,
        choices=constants.UnitSystem.choices,
        default=constants.UnitSystem.METRIC,
    )
    base_value = models.FloatField()


class Ingredient(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    fdc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    base_quanqity = models.FloatField()


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(
        Cuisine, on_delete=models.SET_NULL, null=True, blank=True
    )
    dish_type = models.ForeignKey(
        DishType, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices=constants.RecipeStatus.choices,
        default=constants.RecipeStatus.DRAFT,
    )
    cooking_time = models.DurationField()
    nutritonal_values = models.JSONField("NutritionalValues", default=None)
    difficulty = models.CharField(
        max_length=2,
        choices=constants.RecipeDifficulty.choices,
        default=constants.RecipeDifficulty.EASY,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ingreditents = models.ManyToManyField(Ingredient, through="RecipeIngredients")


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.SmallIntegerField()
    content = models.TextField(blank=True, null=True)
    media = models.URLField(blank=True, null=True)


class RecipeAttachments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    quantity = models.FloatField()


# class Comment(models.Models):
#    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
#    media = models.URLField(max_length=255, blank=True, null=True)
#
# class Ratings(models.Model):
#    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    value =
#
