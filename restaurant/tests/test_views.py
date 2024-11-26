from django.test import TestCase, Client
from restaurant.models import MenuItem
from django.urls import reverse


class MenuItemViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pasta", price=70, inventory=100)

    def test_get_all(self):
        self.set
        client = Client()
        response = client.get(reverse('menu-items'))  # Replace with your view's name
        self.assertEqual(response.status_code, 200)
        