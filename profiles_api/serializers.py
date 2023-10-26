from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(
        max_length=255,
        error_messages={
            'required': 'name is a required field, please provide a name',
            'blank': 'name cannot be empty, please provide a valid value'
        }
    )