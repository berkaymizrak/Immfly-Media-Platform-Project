import random

from core import factories
from core.models import Person, Document, Language
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, IntegrityError
from product.models import Groups, Genre, Channel, Content, ContentPersonRelation

affected_models = [
    Person,
    Document,
    Language,
    Groups,
    Genre,
    Channel,
    Content,
    ContentPersonRelation,
]


class Command(BaseCommand):
    help = 'Generates test data'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING(
            '\nThis command will clear all models\' data and create the test data.'
            '\nThe models that is going to be affected:'
        ))
        for model in affected_models:
            self.stdout.write(self.style.SUCCESS(model.__name__))
        self.stdout.write(self.style.WARNING(
            'This action can not be undo.\n'
        ))
        r = input('Would you like to continue? (y/N): ')
        if r not in ('y', 'Y'):
            raise CommandError('Command exited.')

        for model in affected_models:
            self.stdout.write(self.style.HTTP_SERVER_ERROR('\nDeleting old data: %s' % model.__name__))
            model.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('\nDeleting completed. Creating new data...'))

        self.safe_run_factory(factories.PersonFactory)
        self.safe_run_factory(factories.DocumentFactory)
        call_command('loaddata', 'languages.json')
        self.safe_run_factory(factories.GroupsFactory)
        self.safe_run_factory(factories.GenreFactory)
        self.safe_run_factory(factories.ChannelFactory)
        self.safe_run_factory(factories.ChannelGroupsRelationFactory)
        self.safe_run_factory(factories.ContentFactory)
        self.safe_run_factory(factories.ContentGenreRelationFactory)
        self.safe_run_factory(factories.ContentPersonRelationFactory)
        self.safe_run_factory(factories.ContentFileRelationFactory)

        self.stdout.write(self.style.SUCCESS('\nAll processes successfully finished.'))

    def safe_run_factory(self, factory, times=50):
        for i in range(times):
            while True:
                try:
                    factory()
                    break
                except IntegrityError as e:
                    continue
