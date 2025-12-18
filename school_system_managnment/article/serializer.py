from rest_framework import serializers
from .models import Article
from session.models import Session
from helpers.feltiringRelatedField import FilteredPrimaryKeyRelatedFieldBySchool
class CreateArticleSerializer(serializers.ModelSerializer):
    session = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Session.objects.all() , required=True)
    class Meta:
        model=Article
        fields = '__all__'
        extra_kwargs = {
            'school':{'read_only':True}
            }
    def create(self, validated_data):
        validated_data['school'] = self.context['request'].user.school
        return super().create(validated_data)


class UpdateArticleSerializer(serializers.ModelSerializer):
    session = FilteredPrimaryKeyRelatedFieldBySchool(queryset = Session.objects.all() , required=False)
    class Meta:
        model=Article
        fields = '__all__'
        extra_kwargs = {
            'school':{'read_only':True}
            }



class RetreiveArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Article
        fields = '__all__'
        

class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields = '__all__'
        

