from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Profile

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    last_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')

        user.save()
        return user

class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid email or password")

            user = authenticate(
                request=self.context.get('request'),
                username=user.email,
                password=password,
            )

            if not user:
                raise serializers.ValidationError("Invalid email or password")

        else:
            raise serializers.ValidationError("Must include email and password")

        attrs['user'] = user
        return attrs

class CustomUserDetailsSerializer(UserDetailsSerializer):
    is_spotify = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("is_spotify",)

    def get_is_spotify(self, user):
        return hasattr(user, "spotify")
    
class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserDetailsSerializer(read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Profile
        fields = "__all__"