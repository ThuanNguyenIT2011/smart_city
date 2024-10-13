from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
# from rest_framework.models import Token
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'