# For creating test data
from core.models import *
from core.enums import DocumentTypes
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory
from faker_enum import EnumProvider
from product.enums import ContentPersonRelationTypes
from product.models import *

factory.Faker.add_provider(EnumProvider)


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = factory.Faker('date_of_birth')


class DocumentFactory(DjangoModelFactory):
    class Meta:
        model = Document

    document = factory.Faker('file_path')
    doc_type = factory.Faker('enum', enum_cls=DocumentTypes)


class GroupsFactory(DjangoModelFactory):
    class Meta:
        model = Groups

    name = factory.Faker('name')
    code = factory.Faker('slug')


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker('name')
    age_rate = factory.Faker('word', ext_word_list=[0, 12, 18, 21])


class ChannelFactory(DjangoModelFactory):
    class Meta:
        model = Channel

    code = factory.Faker('slug')
    title = factory.Faker('name')
    language = factory.Iterator(Language.objects.all())
    picture = factory.Faker('file_path')


class ChannelGroupsRelationFactory(DjangoModelFactory):
    class Meta:
        model = Channel.group.through

    channel = factory.Iterator(Channel.objects.all())
    groups = factory.Iterator(Groups.objects.all())


class ContentFactory(DjangoModelFactory):
    class Meta:
        model = Content

    name = factory.Faker('name')
    description = factory.Faker('sentence', nb_words=5, variable_nb_words=True)
    season = factory.Faker('pyint', min_value=1, max_value=4)
    episode = factory.Faker('pyint', min_value=1, max_value=13)
    rating = fuzzy.FuzzyDecimal(0.5, 10)
    channel = factory.Iterator(Channel.objects.all())


class ContentGenreRelationFactory(DjangoModelFactory):
    class Meta:
        model = Content.genre.through

    content = factory.Iterator(Content.objects.all())
    genre = factory.Iterator(Genre.objects.all())


class ContentPersonRelationFactory(DjangoModelFactory):
    class Meta:
        model = Content.person.through

    content = factory.Iterator(Content.objects.all())
    person = factory.Iterator(Person.objects.all())
    relation_type = factory.Faker('enum', enum_cls=ContentPersonRelationTypes)


class ContentFileRelationFactory(DjangoModelFactory):
    class Meta:
        model = Content.file.through

    content = factory.Iterator(Content.objects.all())
    document = factory.Iterator(Document.objects.all())
