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

        factories.ContentFactory(
            channel=self.channel_3_3,
            rating=3,
        )
        factories.ContentFactory(
            channel=self.channel_3_3,
            rating=5,
        )
        factories.ContentFactory(
            channel=self.channel_3_1,
            rating=4.5,
        )
        factories.ContentFactory(
            channel=self.channel_3_1,
            rating=6.5,
        )
        factories.ContentFactory(
            channel=self.channel_3_1,
            rating=7,
        )
        factories.ContentFactory(
            channel=self.channel_3_2,
            rating=4,
        )
        factories.ContentFactory(
            channel=self.channel_3_2,
            rating=2,
        )
        factories.ContentFactory(
            channel=self.channel_3_2,
            rating=9,
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

