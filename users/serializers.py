from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email')


  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    return user
    
  def update(self,instance, validated_data):
      user = User.objects.get(username=validated_data['username'],email=validated_data["email"])
      user.password = make_password(validated_data["password"])
      user.save()
      return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("No Matching Credentials")

class UpdateUser(serializers.Serializer):
    def update(self,instance, validated_data):
      user = User.objects.get(username=validated_data['username'],email=validated_data["email"])
      user.password = make_password(validated_data["password"])
      user.save()
      return user