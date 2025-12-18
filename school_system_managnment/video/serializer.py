from rest_framework import serializers
from .models import Video
from material.models import Media
from material.serializer import CreateMediaSerializer , UpdateMediaSerializer , RetreiveMediaSerializer , ListMediaSerializer
from django.core.files.base import File
class CreateVideoSerializer(serializers.ModelSerializer):
    media = CreateMediaSerializer()
    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        media = validated_data.pop('media')
        media = Media.objects.create(file = media['file'])
        validated_data['media'] = media
        return super().create(validated_data)   
    
class UpdateVideoSerializer(serializers.ModelSerializer):
    media = UpdateMediaSerializer(required = False)
    class Meta:
        model = Video
        fields = '__all__'
    
    def to_internal_value(self, data):
        if data :
            data_copy = data.copy()
            if 'media.file' in data and not isinstance(data['media.file'],File):
                        data_copy.pop('media.file')
            return super().to_internal_value(data_copy)
        return super().to_internal_value(data)
    
    def update(self, instance, validated_data):
        
        media_data = validated_data.pop('media' , None)
        if media_data:
            serializer = UpdateMediaSerializer(instance.media , context = self.context , data = media_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return super().update(instance, validated_data)
    


class RetreiveVideoSerializer(serializers.ModelSerializer):
        media = RetreiveMediaSerializer()
        class Meta:
            model = Video
            fields = '__all__'


class ListVideoSerializer(serializers.ModelSerializer):
        media = ListMediaSerializer()
        class Meta:
            model = Video
            fields = '__all__'
