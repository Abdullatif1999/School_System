from rest_framework import serializers
from .models import Student
from helpers.feltiringRelatedField import FilteredPrimaryKeyRelatedFieldBySchool 
from helpers.createUserHelpers import CreateUserMemberHelper
from clas.models import Clas
from clas.serializer import RetreiveClasSerializer
from user.serializer.user import CreateUserMemberSerializer
class CreateStudentSerializer(serializers.ModelSerializer):
    clas = FilteredPrimaryKeyRelatedFieldBySchool(queryset =Clas.objects.all())
    class Meta:
        model = Student
        fields = ['first_name','last_name','date_of_birth' , 'clas']

class CreateUserStudentSerializer(serializers.ModelSerializer):
    user = CreateUserMemberSerializer(required = True)
    class Meta:
        model = Student
        fields = ['user']
    
    def update(self, instance, validated_data):
        user = CreateUserMemberHelper(instance , validated_data).create_user()
        instance.user = user
        instance.save(update_fields = ['user'])
        return instance
class ListStudentSerializer(serializers.ModelSerializer):
    clas = RetreiveClasSerializer()
    class Meta:
        model = Student
        fields = '__all__'


class RetreiveStudentSerializer(serializers.ModelSerializer):
    clas = RetreiveClasSerializer()
    class Meta:
        model = Student
        fields = '__all__'

class UpdateStudentSerializer(serializers.ModelSerializer):
    clas = FilteredPrimaryKeyRelatedFieldBySchool(queryset =Clas.objects.all()  , required = False)
    class Meta:
        model = Student
        fields = ['first_name','last_name','clas' , 'date_of_birth']