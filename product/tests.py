from product import models
from core import factories
from django.core.management import call_command
from django.test import TestCase

# Create your tests here.


class ChannelContentTestCase(TestCase):
    def setUp(self):
        call_command('loaddata', 'languages.json')
        self.channel_1 = factories.ChannelFactory()
        self.channel_2_1 = factories.ChannelFactory(
            parent=self.channel_1,
        )
        self.channel_3_1 = factories.ChannelFactory(
            parent=self.channel_2_1,
        )
        self.channel_3_2 = factories.ChannelFactory(
            parent=self.channel_2_1,
        )
        self.channel_2_2 = factories.ChannelFactory(
            parent=self.channel_1,
        )
        self.channel_3_3 = factories.ChannelFactory(
            parent=self.channel_2_2,
        )

        genre_1 = factories.GenreFactory(
            age_rate=0,
        )
        genre_2 = factories.GenreFactory(
            age_rate=12,
        )
        genre_3 = factories.GenreFactory(
            age_rate=12,
        )
        genre_4 = factories.GenreFactory(
            age_rate=18,
        )
        genre_5 = factories.GenreFactory(
            age_rate=21,
        )

        self.content_1 = factories.ContentFactory(
            channel=self.channel_3_3,
            rating=3,
        )
        self.content_2 = factories.ContentFactory(
            channel=self.channel_3_3,
            rating=5,
        )
        self.content_3 = factories.ContentFactory(
            channel=self.channel_3_1,
            rating=4.5,
        )
        self.content_4 = factories.ContentFactory(
            channel=self.channel_3_1,
            rating=6.5,
        )
        self.content_5 = factories.ContentFactory(
            channel=self.channel_3_1,
            rating=7,
        )
        self.content_6 = factories.ContentFactory(
            channel=self.channel_3_2,
            rating=4,
        )
        self.content_7 = factories.ContentFactory(
            channel=self.channel_3_2,
            rating=2,
        )
        self.content_8 = factories.ContentFactory(
            channel=self.channel_3_2,
            rating=9,
        )

        factories.ContentGenreRelationFactory(
            content=self.content_1,
            genre=genre_1,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_1,
            genre=genre_2,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_1,
            genre=genre_3,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_1,
            genre=genre_4,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_2,
            genre=genre_1,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_3,
            genre=genre_3,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_4,
            genre=genre_4,
        )
        factories.ContentGenreRelationFactory(
            content=self.content_5,
            genre=genre_5,
        )

        """
        channel_1
        ├── channel_2_1
        │   ├── channel_3_1
        │   └── channel_3_2
        ├── channel_2_2
        │   └── channel_3_3
        """

    def test_deepest_channel(self):
        self.assertEqual(self.channel_1.deepest_channel(), False)
        self.assertEqual(self.channel_2_1.deepest_channel(), False)
        self.assertEqual(self.channel_3_1.deepest_channel(), True)
        self.assertEqual(self.channel_3_2.deepest_channel(), True)
        self.assertEqual(self.channel_2_2.deepest_channel(), False)
        self.assertEqual(self.channel_3_3.deepest_channel(), True)

    def test_get_rating(self):
        self.assertEqual(self.channel_1.get_rating(), 4.75)
        self.assertEqual(self.channel_2_1.get_rating(), 5.5)
        self.assertEqual(self.channel_3_1.get_rating(), 6)
        self.assertEqual(self.channel_3_2.get_rating(), 5)
        self.assertEqual(self.channel_2_2.get_rating(), 4)
        self.assertEqual(self.channel_3_3.get_rating(), 4)

    def test_get_age_rate(self):
        self.assertEqual(self.content_1.get_age_rate(), 18)
        self.assertEqual(self.content_2.get_age_rate(), 0)
        self.assertEqual(self.content_3.get_age_rate(), 12)
        self.assertEqual(self.content_4.get_age_rate(), 18)
        self.assertEqual(self.content_5.get_age_rate(), 21)
        self.assertEqual(self.content_6.get_age_rate(), None)
        self.assertEqual(self.content_7.get_age_rate(), None)
        self.assertEqual(self.content_8.get_age_rate(), None)

