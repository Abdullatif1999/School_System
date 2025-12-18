from rest_framework import serializers
from .models import Clas
from teacher.models import Teacher
from subject.serializer import ListSubjectSerializer
from school.serializer import RetrieveSchoolSerializer
class CreateClasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clas
        fields = ['name']

    def create(self, validated_data):
        validated_data['school'] = self.context.school
        return super().create(validated_data)


class ListClasSerializer(serializers.ModelSerializer):
      school = RetrieveSchoolSerializer()
      subjects = ListSubjectSerializer(many=True)
      class Meta:
            model = Clas
            fields = ['id','name', 'school', 'subjects']

class UpdateClasSerializer(serializers.ModelSerializer):
       class Meta:
                model = Clas
                fields = ['name']


class RetreiveClasSerializer(serializers.ModelSerializer):
        school = RetrieveSchoolSerializer()
        class Meta:
            model = Clas
            fields = '__all__'