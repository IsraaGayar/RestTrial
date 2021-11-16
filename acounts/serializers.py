from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = ('email', 'username', 'password', 'password2')
        fields = '__all__'

    def save(self, **kwargs):
        # print(self.validated_data('password2'))
        user = User(email=self.validated_data.get('email'),
                    username=self.validated_data.get('username')
                    )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError(
            {
                 'password': "Password doesn't match"
            })
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()
