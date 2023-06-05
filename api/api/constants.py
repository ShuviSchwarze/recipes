from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _


class RecipeStatus(models.TextChoices):
    DRAFT = "DR", _("Draft")
    AWAITING = "AW", _("Awaiting")
    NEEDED_CHANGES = "NC", _("Needed Changes")
    REJECTED = "RE", _("Rejected")
    PUBLISHED = "PU", _("Published")
    ARCHIVED = "AR", _("Archived")
    DELETED = "DE", _("Deleted")


class RecipeDifficulty(models.TextChoices):
    NA = "NA", _("NA")
    VERY_EASY = "VE", _("Very Easy")
    EASY = "EA", _("Easy")
    MODERATE = "MO", _("Moderate")
    HARD = "HA", _("Hard")
    VERY_HARD = "VH", _("Very Hard")


class UnitType(models.TextChoices):
    MASS = "MA", _("MASS")
    VOLUME = "VO", _("VOLUME")


class UnitSystem(models.TextChoices):
    METRIC = "ME", _("METRIC")
    IMPERIAL = "IM", _("IMPERIAL")
    US = "US", _("US")


# class Rating(Enum):
