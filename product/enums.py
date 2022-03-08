from django.db import models
from django.utils.translation import gettext_lazy as _


class ContentPersonRelationTypes(models.TextChoices):
    AUTHOR = "author", _("Author")
    DIRECTOR = "director", _("Director")
    CAST = "cast", _("Cast")
