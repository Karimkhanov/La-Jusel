from rest_framework import serializers
from .models import showtimes


class showtimesSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = showtimes
        fields = '__all__'
