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


