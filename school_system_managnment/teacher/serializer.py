from rest_framework import serializers

from helpers.createUserHelpers import CreateUserMemberHelper
from user.models import User
from .models import Teacher
from subject.models import Subject
from subject.serializer import RetreiveSubjectSerializer
from user.serializer.user import CreateUserMemberSerializer
from helpers.feltiringRelatedField import FilteredPrimaryKeyRelatedFieldBySchool



class CreateTeacherSerializer(serializers.ModelSerializer):
    subjects = FilteredPrimaryKeyRelatedFieldBySchool(many=True,queryset=Subject.objects.all(),write_only=True)
    class Meta:
        model = Teacher
        fields = ['specialization' , 'subjects' ,'first_name' , 'last_name' , 'school']
        extra_kwargs = {'school':{'read_only':True}}
    

    def create(self, validated_data):
        subjects = validated_data.pop('subjects')
        validated_data['school'] = self.context['request'].user.school
        teacher = super().create(validated_data)
        teacher.subjects.set(subjects)
        return teacher




class CreateUserTeacherSerializer(serializers.ModelSerializer):
    user = CreateUserMemberSerializer(required = True)
    class Meta:
        model = User
        fields = ['user']
    def update(self, instance, validated_data):
        user = CreateUserMemberHelper(instance , validated_data).create_user()
        instance.user = user
        instance.save(update_fields =['user'])
        return instance

class RetreiveTeacherSerializer(serializers.ModelSerializer):
    subjects = RetreiveSubjectSerializer(many = True)
    class Meta:
        model = Teacher
        fields = '__all__'


class UpdateTeacherSerializer(serializers.ModelSerializer):
    subjects = FilteredPrimaryKeyRelatedFieldBySchool(many=True,queryset=Subject.objects.all(),write_only=True , required = False)
    class Meta:
        model = Teacher
        exclude = ['school' , 'user']


    def update(self, instance, validated_data):
        subjects = validated_data.pop('subjects' , None)
        teacher = super().update(instance, validated_data)
        if subjects and len(subjects):
            teacher.subjects.set(subjects)
        return teacher
    

class ListTeacherSerializer(serializers.ModelSerializer):
    subjects = RetreiveSubjectSerializer(many = True)
    class Meta:
        model = Teacher
        fields = '__all__'

