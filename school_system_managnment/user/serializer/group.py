from rest_framework import serializers
from django.contrib.auth.models import Group , Permission
from .permission import ListPermissionSerializer
class ListGroupSerializer(serializers.ModelSerializer):
    permissions = ListPermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'
        

class CreateGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(queryset = Permission.objects.all() , many=True)
    class Meta:
        model = Group
        fields = '__all__'
        

    def create(self, validated_data):
        permissions = validated_data.pop('permissions')
        group =  super().create(validated_data)
        group.permissions.set(permissions)
        return group
    

class UpdateGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(queryset = Permission.objects.all() , many=True)
    class Meta:
        model = Group
        fields = '__all__'
        

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions')
        instance.name = validated_data['name']
        old_instance = instance.permissions.all()
        for one in old_instance:
            one.delete()
        instance.permissions.set(permissions)
        instance.save()
        return instance
    

class RetreiveGroupSerializer(serializers.Serializer):
        permissions = ListPermissionSerializer(many=True)
        class Meta:
            model = Group
            fields = '__all__'
            
