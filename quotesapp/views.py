from django.shortcuts import render, redirect
from quotesapp.models import QuoteCategory
from rest_framework import serializers
# Create your views here.

class QuoteCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField()
    class Meta:
        model = QuoteCategory
        fields = ["id", "category_name"]


def reverse(request):
    return redirect('')



def index(request):
    quote_categories = QuoteCategory.objects.all()
    context = QuoteCategorySerializer(quote_categories, many=True).data
    final_result = {}
    final_result["data"] = context
    print(final_result)
    return render(request, 'index.html', final_result)

