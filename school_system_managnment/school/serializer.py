from rest_framework import serializers
from .models import School
from user.serializer.user import CreateSuperUserSerializer
from user.models import User
from employee.models import Employee

class CreateSchoolSerializer(serializers.ModelSerializer):
    user = CreateSuperUserSerializer(write_only = True )
    class Meta:
        model = School
        fields =['name','type','user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        employee_data = {'role' : 'Manager' , 'first_name':user_data['first_name'] , 'last_name':user_data['last_name']}
        school = super().create(validated_data)
        user_data['school'] = school
        serializer = CreateSuperUserSerializer(data=user_data)
        user = serializer.create(user_data)
        Employee.objects.create(**employee_data , user= user , school = school)
        return user




class RetrieveSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name' , 'type']