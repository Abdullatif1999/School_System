from rest_framework import serializers
from ..models import Quiz
from .optionSerializer import CreateOptionSerializer , RetreiveOptionSerializer , ListOptionSerializer,UpdateOptionSerializer
class CreateQuizSerializer(serializers.ModelSerializer):
    options = CreateOptionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = '__all__'
        extra_kwargs = {
                'school': {'read_only':True}
            }
    def create(self, validated_data):
        options = validated_data.pop('options')
        validated_data['school'] = self.context['request'].user.school
        quiz = super().create(validated_data)
        for option in options:
            option['quiz'] = quiz
            serializer = CreateOptionSerializer(data = option , context = {'quiz':quiz})
            option = serializer.create(option)
        return quiz
    

class RetreiveQuizSerializer(serializers.ModelSerializer):
    options = RetreiveOptionSerializer(many=True)
    class Meta:
        model = Quiz
        exclude = ['polymorphic_ctype']


class ListQuizSerializer(serializers.ModelSerializer):
    options = ListOptionSerializer(many=True)
    class Meta:
        model = Quiz
        exclude = ['polymorphic_ctype']

class UpdateQuizSerializer(serializers.ModelSerializer):
    options = UpdateOptionSerializer(many=True , required = False)
    class Meta:
        model = Quiz
        fields = '__all__'
        extra_kwargs = {
                'school': {'read_only':True}
            }
    def update(self, instance, validated_data):
        options = validated_data.pop('options' , None)
        quiz = super().update(instance, validated_data)
        if options:
            old_options = instance.options.all()
            for option in old_options:
                option.delete() 
            for option in options:
                option['quiz'] = quiz
                serializer = CreateOptionSerializer(data = option , context = {'quiz':quiz})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return quiz