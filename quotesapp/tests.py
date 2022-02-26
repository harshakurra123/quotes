from django.test import TestCase
from .models import Quotes, QuoteCategory
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class ViewsTestCase(TestCase):

    def setUp(self):
        quote_category_life = QuoteCategory.objects.create(category_name="life_quotes")
        quote_category_success = QuoteCategory.objects.create(category_name="life_success")
        Quotes.objects.create(quote_title="life", quote_description="Life is what happens when you're busy making other plans", quote_category_id=quote_category_life.id)
        Quotes.objects.create(quote_title="success", quote_description="Do what you can with all you have, wherever you are", quote_category_id=quote_category_success.id)

    def test_quotes(self):
        life = Quotes.objects.get(quote_title="life")
        success = Quotes.objects.get(quote_title="success")
        self.assertEqual(life.quote_description, "Life is what happens when you're busy making other plans")
        self.assertEqual(success.quote_description, "Do what you can with all you have, wherever you are")


    # def test_index_loads_properly(self):
    #     response = self.client.get('127.0.0.1:8001')
    #     print(response)
    #     self.assertEqual(response.status_code, 200)



class PlayerFormTest(LiveServerTestCase):

  def testform(self):
      selenium = webdriver.Chrome()
      #Choose your url to visit
      selenium.get('http://127.0.0.1:8001/')
      player_name = selenium.find_element_by_id('id_title')
