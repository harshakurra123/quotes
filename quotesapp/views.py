from django.shortcuts import render, redirect
from quotesapp.models import QuoteCategory
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class QuoteCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField()
    class Meta:
        model = QuoteCategory
        fields = ["id", "category_name"]


def reverse(request):
    return redirect('')



def index(request):
    print('jkgdjhfg')
    user = request.user
    # if user.is_authenticated:
    quote_categories = QuoteCategory.objects.all()
    context = QuoteCategorySerializer(quote_categories, many=True).data
    final_result = {}
    final_result["data"] = context
    print(final_result)
    return render(request, 'index.html', final_result)
    # else:
    #     return render(request, 'index.html')


class QuoteCategoryAPI(APIView):
    """
    QuoteCategoryAPI.
    """
    def get(self, request):
        quote_categories = QuoteCategory.objects.all()
        quote_categories_ser = QuoteCategorySerializer(quote_categories, many=True).data
        return Response(quote_categories_ser, status=200)


from urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2


class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('picture', 'picture'),
        ('email', 'email')
    ]

    def authorization_url(self):
        return 'https://' + self.setting('DOMAIN') + '/authorize'

    def access_token_url(self):
        return 'https://' + self.setting('DOMAIN') + '/oauth/token'

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['user_id']

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get('id_token')
        jwks = request.urlopen('https://' + self.setting('DOMAIN') + '/.well-known/jwks.json')
        issuer = 'https://' + self.setting('DOMAIN') + '/'
        audience = self.setting('KEY')  # CLIENT_ID
        payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)

        return {'username': payload['nickname'],
                'first_name': payload['name'],
                'picture': payload['picture'],
                'user_id': payload['sub'],
                'email': payload['email']}

from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)