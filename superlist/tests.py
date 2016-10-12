from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolvers(self):
        found = resolve('/superlist/')
        self.assertEqual(found.func, home_page)