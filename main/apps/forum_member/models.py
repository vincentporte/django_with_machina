from django.core.validators import RegexValidator
from django.db import models
from machina.apps.forum_member.abstract_models import AbstractForumProfile


class ForumProfile(AbstractForumProfile):
    is_ambassador = models.BooleanField(verbose_name="ambassador", default=False)

    linkedin_url = models.URLField(
        verbose_name="linked profile",
        default=None,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex="^https:\/\/www\.linkedin\.[a-z]{2,3}",
                message="Url doesn't comply",
            ),
        ],
    )
