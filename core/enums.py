from django.db import models
from django.utils.translation import gettext_lazy as _


class DocumentTypes(models.TextChoices):
    VIDEO = "video", _("Video")
    PDF = "pdf", _("PDF")
    TEXT = "text", _("Text")
    PHOTO = "photo", _("Photo")

