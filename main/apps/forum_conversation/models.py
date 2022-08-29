# Custom models should be declared before importing
# django-machina models
from django.db import models
from machina.apps.forum_conversation.abstract_models import AbstractPost, AbstractTopic
from machina.core.loading import get_class

OpenForumsPostManager = get_class("forum_conversation.managers", "OpenForumsPostManager")
OpenForumsPostQuerySet = get_class("forum_conversation.managers", "OpenForumsPostQuerySet")
ApprovedManager = get_class("forum_conversation.managers", "ApprovedManager")


class Topic(AbstractTopic):
    category = models.ForeignKey(
        "forum_category.ForumCategory",
        on_delete=models.SET_NULL,
        related_name="categories",
        verbose_name=("Topic category"),
        default=None,
        null=True,
        blank=True,
    )


class Post(AbstractPost):
    objects = models.Manager()
    approved_objects = ApprovedManager()
    openforums_objects = OpenForumsPostManager.from_queryset(OpenForumsPostQuerySet)()
