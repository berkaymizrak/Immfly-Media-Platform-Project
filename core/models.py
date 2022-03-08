from core import enums
from django.db import models
from django.utils.translation import gettext_lazy as _
import os


# Create your models here.


class AbstractModel(models.Model):
    is_deleted = models.BooleanField(default=False, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class Person(AbstractModel):
    """

    """
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=255,
    )
    last_name = models.CharField(
        default='',
        verbose_name=_('Last Name'),
        max_length=255,
        blank=True,
    )
    date_of_birth = models.DateField(
        default=None,
        verbose_name=_('Birthday'),
        null=True,
        blank=True,
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __str__(self):
        return '%s' % self.get_full_name()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


def get_file_path(obj, fname):
    return os.path.join(
        'media',
        'documents',
        obj.doc_type,
        fname,
    )


class Document(AbstractModel):
    document = models.FileField(
        upload_to=get_file_path,
        verbose_name=_('Document'),
    )
    doc_type = models.CharField(
        choices=enums.DocumentTypes.choices,
        verbose_name=_('Document Type'),
        max_length=20,
    )

    class Meta(AbstractModel.Meta):
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self):
        return '%s' % self.document and self.document.name


class Language(AbstractModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        help_text='',
    )
    code = models.CharField(max_length=2, unique=True, verbose_name=_('Code'))

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)
