"""Flexible page"""
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page


class FlexPage(Page):
    templates = "flex/flex_page.html"

    # # @todo add strean\mfields
    # content = StreamFields()
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"