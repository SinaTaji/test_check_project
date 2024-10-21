from drf_spectacular.utils import extend_schema
from home.models import Staff
from home.serializers import AdminStaffSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class StaffViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Staff.objects.all().order_by('first_name', 'last_name')
    serializer_class = AdminStaffSerializer

    @extend_schema(
        summary="Retrieve a list of staff members",
        description="this api use to show list of all staff members",
        responses={200: AdminStaffSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Retrieve a specific staff member",
        description="this api use to retrieve a specific staff member and show all data",
        responses={200: AdminStaffSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new staff member",
        description="this api use to create a new staff member",
        request=AdminStaffSerializer,
        responses={201: AdminStaffSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Update a specific staff member",
        description="this api use to update a specific staff member ",
        request=AdminStaffSerializer,
        responses={200: AdminStaffSerializer},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a specific staff member",
        description="this api use to delete a specific staff member",
        responses={204: None},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
