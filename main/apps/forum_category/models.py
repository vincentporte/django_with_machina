from django.db import models


class ForumCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name", blank=False, null=False)

    objects = models.Manager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
