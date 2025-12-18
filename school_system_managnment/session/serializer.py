from rest_framework import serializers
from .models import Session
from subject.models import Subject
from helpers.feltiringRelatedField import FilteredPrimaryKeyRelatedFieldBySchool
class CreateSessionSerializer(serializers.ModelSerializer):
    subject = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Subject.objects.all() , required = True)
    class Meta:
        model = Session
        fields = '__all__'
        extra_kwargs = {
            'school' : {"read_only": True}
            }


    def create(self, validated_data):
        validated_data['school'] = self.context['request'].user.school
        return super().create(validated_data)

class UpdateSessionSerializer(serializers.ModelSerializer):
    subject = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Subject.objects.all() , required = True)
    class Meta:
        model = Session
        exclude = ['id']
        extra_kwargs = {
            'school' : {"read_only": True}
            }
        
        
        
class RetreiveSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class ListSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

