from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format = None):
        """Return a list of APIViews features"""
        
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            "It's mapped manually to URLs",
        ]
        
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview 
        })
        
    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name') # type: ignore
            message = f'Hello {name}'
            return Response({
                'message': message
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({
            "method": "PUT"
        }, status=status.HTTP_200_OK)
        
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({
            "method": "PATCH"
        }, status=status.HTTP_200_OK)
        
    def delete(self, request, pk=None):
        """Handle a delete of an object"""
        return Response({
                "method": "DELETE"
            }, status=status.HTTP_200_OK)
        
        
        