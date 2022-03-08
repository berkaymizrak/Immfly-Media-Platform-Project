from core.models import AbstractModel, Person, Language, Document
from product import enums
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Groups(AbstractModel):
    """

    """
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text='',
    )
    code = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Group Code"),
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return '%s' % self.name


class Genre(AbstractModel):
    """

    """
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text='',
    )
    age_rate = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Age Rate"),
        help_text='Please enter the minimum age rate to reach contents of this genre.',
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return '%s' % self.name


class Channel(AbstractModel):
    """

    """
    code = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Channel Code"),
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=_("Parent"),
        blank=True,
        null=True,
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        verbose_name=_("Language"),
    )
    group = models.ManyToManyField(
        Groups,
        verbose_name=_("Group"),
        blank=True,
    )
    picture = models.ImageField(
        upload_to='media/channels',
        verbose_name=_("Picture"),
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self):
        return '%s' % self.title

    def get_author_list(self):
        content_ids = self.content_set.values_list('id', flat=True)
        return ContentPersonRelation.objects.filter(
            content_id__in=content_ids,
            relation_type=enums.ContentPersonRelationTypes.AUTHOR,
        ).values_list(
            'person__first_name',
            flat=True,
        )

    def get_rating(self):
        return self.content_set.values_list('rating', flat=True)


class Content(AbstractModel):
    """

    """
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text='',
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )
    season = models.PositiveIntegerField(
        verbose_name=_("Season"),
    )
    episode = models.PositiveIntegerField(
        verbose_name=_("Episode"),
    )
    rating = models.DecimalField(
        default=Decimal('0'),
        verbose_name=_("Rating"),
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('10'))],
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        verbose_name=_("Channel"),
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name=_("Genre"),
        blank=True,
    )
    file = models.ManyToManyField(
        Document,
        verbose_name=_("Document"),
        blank=True,
    )
    person = models.ManyToManyField(
        Person,
        through="ContentPersonRelation",
        through_fields=("content", "person"),
        verbose_name=_("Person"),
        blank=True,
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _("Content")
        verbose_name_plural = _("Contents")

    def __str__(self):
        return '%s' % self.name

    def get_age_rate(self):
        print(self.genre.through.all())


class ContentPersonRelation(AbstractModel):
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        verbose_name=_("Content"),
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name=_("Person"),
    )
    relation_type = models.CharField(
        choices=enums.ContentPersonRelationTypes.choices,
        verbose_name=_("Content Person Relation Type"),
        max_length=20,
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _("Content Person Relation")
        verbose_name_plural = _("Content Person Relations")
        constraints = [
            models.UniqueConstraint(
                fields=["content", "person", "relation_type", ],
                name="%(app_label)s_%(class)s_unique_content_person_relation_type",
            )
        ]

    def __str__(self):
        return "%s - %s (%s)" % (self.content.name, self.person.get_full_name(), self.get_relation_type_display())
