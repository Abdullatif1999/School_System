from rest_framework import serializers


class FilteredPrimaryKeyRelatedFieldBySchool(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super().get_queryset()   
        if request and request.user and request.user.school:
            return queryset.filter(school=request.user.school)
        return queryset.none()