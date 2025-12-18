from rest_framework import serializers
from .models import Employee
from user.serializer.user import CreateUserMemberSerializer
from helpers.createUserHelpers import CreateUserMemberHelper

class CreateEmployeeSerializer(serializers.ModelSerializer):
    school = serializers.CharField(read_only = True)
    class Meta:
        model = Employee
        exclude = ['user']
    def create(self, validated_data):
        validated_data['school'] = self.context['user'].school 
        return super().create(validated_data)
    

class RetrieveEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ListEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UpdateEmployeeSerializer(serializers.ModelSerializer):
     class Meta:
        model = Employee
        exclude = ['school' , 'user']


class CreateUserEmployeeSerializer(serializers.ModelSerializer): 
    user = CreateUserMemberSerializer(required = True)
    class Meta:
        model = Employee
        fields = [ 'user']

    def update(self, instance, validated_data):
        user = CreateUserMemberHelper(instance , validated_data).create_user()
        instance.user = user
        instance.save()
        return instance

