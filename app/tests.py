from rest_framework.test import APITestCase


class DrinkTest(APITestCase):
    def test_vodka(self):
        data = self.client.post('/drinks/', {
            'name': 'Vodka',
            'volume': 700,
            'proof': 40
        }).data
        self.assertEqual(data['alcohol'], 280)

    def test_beer(self):
        data = self.client.post('/drinks/', {
            'name': 'Beer',
            'volume': 500,
            'proof': 4
        }).data
        self.assertEqual(data['alcohol'], 20)
