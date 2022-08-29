from django.db import models


class ForumKind(models.TextChoices):
    PRIVATE = ("PRIVATE", "Groupe privé")
    PUBLIC = ("PUBLIC", "Groupe publique")
    OPENFORUM = ("OPENFORUM", "Forum ouvert")
