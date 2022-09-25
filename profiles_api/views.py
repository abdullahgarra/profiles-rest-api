from rest_framework.views import APIView
from rest_framework.response import Response


#hello world api view

class HelloApiView(APIView):
    '''test api view'''

    def get(self, request, format = None):
        '''returns a list of apiview features'''
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello', 'an apiview':an_apiview})
