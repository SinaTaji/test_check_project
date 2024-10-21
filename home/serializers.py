from rest_framework import serializers
from .models import EntryAndExit, Staff


class EntryAndExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryAndExit
        fields = '__all__'
        read_only_fields = ['entry', 'exit', 'day']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class AdminStaffSerializer(StaffSerializer):
    staff = EntryAndExitSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'staff']
