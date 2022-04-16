from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from post_api.models import Post
from post_api.serializers import SimplePostSerializer
# User Serializer
class UserSerializer(serializers.ModelSerializer):
  post = SimplePostSerializer(read_only=True, many=True)

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'post', 'liked_post')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email', 'post', 'liked_post')


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
    post = SimplePostSerializer(read_only=True, many=True)
    liked_post = SimplePostSerializer(read_only=True, many=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("No Matching Credentials")

class UpdateUser(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'username', 'password', 'email', 'post', 'liked_post')

    def update(self,instance, validated_data):
      user = User.objects.get(username=validated_data['username'],email=validated_data["email"])
      user.password = make_password(validated_data["password"])
      user.save()
      return user

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'