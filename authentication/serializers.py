from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        
        if not username.isalnum():  # username should not contain any special charater like " !, @, #, $, &, *, -, _, " etc.
            raise serializers.ValidationError('username should only contain alphanumaric characters')
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)