from rest_framework import serializers
from rolepermissions.roles import assign_role

from apps.users.models.users import User as CustomUser
from apps.users.roles import User, Owner


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'language', 'phone_number', 'location']


class UserRoleField(serializers.ChoiceField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        if data == 'owner':
            return Owner()
        elif data == 'user':
            return User()
        raise serializers.ValidationError('Invalid role')


# class SignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     role = UserRoleField(choices=[('owner', 'Owner'), ('user', 'User')])
#
#     def create(self, validated_data):
#         role = validated_data.pop('role')  # Remove the 'role' field from the validated data
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         user.language = validated_data['language']
#         user.phone_number = validated_data['phone_number']
#         user.location = validated_data['location']
#         user.save()
#
#         # Assign the selected role to the user
#         if role == 'owner':
#             assign_role(user, Owner)
#         elif role == 'user':
#             assign_role(user, User)
#
#         return user
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password', 'role', 'language', 'phone_number', 'location']

class SignupSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[('owner', 'Owner'), ('user', 'User')], write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'language', 'phone_number', 'location']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')  # Remove 'role' from validated data
        user = CustomUser.objects.create_user(**validated_data)
        assign_role(user, role)  # Assign role to the user
        return user