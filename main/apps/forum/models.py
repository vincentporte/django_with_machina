from django.db import models
from machina.apps.forum.abstract_models import AbstractForum

from .enums import ForumKind


class Forum(AbstractForum):
    moderators_group = models.OneToOneField(
        "auth.Group",
        verbose_name="moderators",
        default=None,
        editable=True,
        related_name="moderators_group",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    contributors_group = models.OneToOneField(
        "auth.Group",
        verbose_name="contributors",
        default=None,
        editable=True,
        related_name="contributors_group",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    kind = models.CharField(
        verbose_name="Type",
        max_length=10,
        choices=ForumKind.choices,
        default=ForumKind.PUBLIC,
    )
