from rest_framework import serializers
from ..models import User
from django.contrib.auth.models import Group
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields =  ['first_name' , 'last_name' , 'phone' , 'city'  , 'email' , 'password' , 'groups' , 'school' ]

    def create(self, validated_data):
        groups = None
        if 'groups' in validated_data:
            groups = validated_data.pop('groups')
        user = User.objects.create_user(validated_data.pop("email") , validated_data.pop("password"),**validated_data)
        if groups:
            user.groups.set(groups)
        return user


class CreateUserMemberSerializer(CreateUserSerializer):
    class Meta(CreateUserSerializer.Meta):
        extra_kwargs = {
            'first_name':{'read_only':True},
            'last_name':{'read_only':True},
            'school':{'read_only':True},
            }

    # def create(self, validated_data):
    #     groups = validated_data.pop('groups')
    #     user = User.objects.create_user(validated_data.pop("email") , validated_data.pop("password"),**validated_data)
    #     user.groups.set(groups)
    #     return user


class CreateSuperUserSerializer(CreateUserSerializer):
    class Meta(CreateUserSerializer.Meta):
        extra_kwargs = {
            'school':{'read_only':True},
            'groups':{'read_only' : True}
            }
    def create(self, validated_data):
        user = User.objects.create_superuser(validated_data.pop("email") , validated_data.pop("password"),**validated_data)
        return user



class RetreiveUserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset = Group.objects.all() , many=True)
    class Meta:
        model = User
        fields =  ['first_name' , 'last_name' , 'phone' , 'city' , 'school' , 'email' , 'groups']




class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email' , 'password']
        