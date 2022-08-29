from django.db import models

from main.apps.forum.enums import ForumKind


class OpenForumsPostQuerySet(models.QuerySet):
    def in_category(self, category_id):
        if category_id:
            return self.filter(topic__category=category_id)
        return self


class OpenForumsPostManager(models.Manager):
    def get_queryset(self):
        """Returns all the approved topics or posts."""
        qs = super().get_queryset()
        return (
            qs.filter(topic__forum__kind=ForumKind.OPENFORUM)
            .order_by("-created")
            .select_related("topic", "topic__category")
        )
