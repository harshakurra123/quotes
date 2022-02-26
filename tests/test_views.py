from django.test import TestCase
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        print("hhjxj")
        response = self.client.get('127.0.0.1:8001')
        self.assertEqual(response.status_code, 200)