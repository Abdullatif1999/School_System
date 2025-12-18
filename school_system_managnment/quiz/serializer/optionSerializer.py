from rest_framework import serializers
from ..models import Option
class CreateOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['text' , 'is_success']


    def create(self, validated_data):
        validated_data['quiz'] = self.context['quiz']
        return super().create(validated_data)
    

class RetreiveOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id','text','is_success']


class ListOptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Option
            fields = ['id','text','is_success']


class UpdateOptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Option
            fields = ['id','text','is_success']