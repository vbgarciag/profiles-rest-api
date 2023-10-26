#from dataclasses import fields
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(
        max_length=10,
        error_messages={
            'required': 'name is a required field, please provide a name',
            'blank': 'name cannot be empty, please provide a valid value'
        }
    )
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                },
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( # type: ignore
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    
# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """Serializes profile feed items"""

#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         extra_kwargs = {'user_profile': {'read_only': True}}