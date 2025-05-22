from rest_framework import serializers
from .models import user

class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=('id',
                'name',
                'email',
                'age')

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name must be a non-empty string.")
        return value

    def validate_age(self, value):
        if not (0 <= value <= 120):
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value

    def validate_email(self, value):
        if user.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already exists.")
        return value