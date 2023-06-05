from enum import Enum


class RecipeStatus(Enum):
    DRAFT = "Draft"
    AWAITING = "Awaiting"
    NEEDED_CHANGES = "Needed Changes"
    REJECTED = "Rejected"
    PUBLISHED = "Published"
    ARCHIVED = "Archived"
    DELETED = "Deleted"


class DifficultyLv(Enum):
    NA = 0
    VERY_EASY = 1
    EASY = 2
    MODERATE = 3
    HARD = 4
    VERY_HARD = 5


class UnitType(Enum):
    MASS = 0
    VOLUME = 1


class UnitSystem(Enum):
    METRIC = 0
    IMPERIAL = 1
    US = 2


# class Rating(Enum):
