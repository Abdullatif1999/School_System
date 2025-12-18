from rest_framework import serializers
from .models import Media
from django.http.request import HttpRequest
import os
class CreateMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['file']


class UpdateMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['file']

    def update(self, instance, validated_data):
        os.remove(instance.file.path)
        return super().update(instance, validated_data)


class RetreiveMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['file' ]


class ListMediaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Media
            fields = ['file' ]