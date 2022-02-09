from django.db import models

# Create your models here.

class QuoteCategory(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'quote_category'


class Quotes(models.Model):
    quote_category = models.ForeignKey(QuoteCategory, on_delete=models.CASCADE)
    quote_description = models.CharField(max_length=500)
    quote_title = models.CharField(max_length=100)

    class Meta:
        db_table = 'quotes'

