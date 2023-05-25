from django.test import TestCase
from django.urls import reverse


class CommandURLTest(TestCase):

    def test_command_home_url_is_correct(self):
        url = reverse('commands:home')
        self.assertEqual(url, '/')

    def test_command_language_url_is_correct(self):
        url = reverse('commands:language', kwargs={'language_id': 1})
        self.assertEqual(url, '/commands/language/1/')

    def test_command_detail_url_is_correct(self):
        url = reverse('commands:command', kwargs={'id': 1})
        self.assertEqual(url, '/commands/1/')
