from rest_framework import serializers
from .models import Subject
from clas.models import Clas
from helpers.feltiringRelatedField import FilteredPrimaryKeyRelatedFieldBySchool

class CreateSubjectSerializer(serializers.ModelSerializer):
    clas = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Clas.objects.all())
    class Meta:
            model = Subject
            fields = '__all__'
    
class RetreiveSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'



class UpdateSubjectSerializer(serializers.ModelSerializer):
    clas = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Clas.objects.all())
    class Meta:
        model = Subject
        fields = '__all__'


class ListSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ['clas']

