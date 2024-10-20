from rest_framework import serializers
from .models import EntryAndExit, Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class EntryAndExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryAndExit
        fields = '__all__'
        read_only_fields = ['entry', 'exit', 'day']
