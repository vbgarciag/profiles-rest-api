from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
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
            name = serializer.validated_data.get('name')  # type: ignore
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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""

        a_viewset = [
            'uses actions (list, create, retrieve, update, partial update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({
            "message": "Hello!",
            "a_viewset": a_viewset
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name", '')  # type: ignore
            message = f'hello {name}'

            return Response({
                message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handling creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnProfile,
        IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile feed items"""
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnFeedItem,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged-in user"""
        return super().perform_create(serializer.save(user_profile=self.request.user))


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
