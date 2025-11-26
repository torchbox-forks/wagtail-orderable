from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from wagtailorderable.models import Orderable


class HomePage(Page):
    pass


class Book(Orderable):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("title"), FieldPanel("author"), FieldPanel("cover_photo")]

    def __str__(self):
        return self.title
