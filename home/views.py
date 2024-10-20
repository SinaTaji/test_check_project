from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import EntryAndExit, Staff
from .serializers import EntryAndExitSerializer, StaffSerializer


class StaffListAPIView(ListAPIView):
    """
    this endpoint is used to list all Staffs
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class EntryApiView(CreateAPIView):
    """
    this endpoint is used to create a new Entry and need staff_id in request body
    """
    queryset = EntryAndExit.objects.prefetch_related('staff').all()
    serializer_class = EntryAndExitSerializer

    def create(self, request, *args, **kwargs):
        """
        hear we need staff_id in request body
        """
        now = timezone.now()
        staff_id = request.data.get('staff_id')
        try:
            staff = Staff.objects.get(id=staff_id)
        except Staff.DoesNotExist:
            return Response({'detail': 'کارمند یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

        record = EntryAndExit.objects.filter(staff=staff, day=now.date()).last()
        if record:
            if not record.is_checked_out():
                return Response({'detail': 'کارمند پس از ورود خارج نشده'}, status=status.HTTP_404_NOT_FOUND)
            entry_record = EntryAndExit.objects.create(staff=staff, day=now.date())
            entry_record.entry = now.time()
            entry_record.save()
            return Response('ورود با موفقیت ثبت شد', status=status.HTTP_201_CREATED)
        entry_record = EntryAndExit.objects.create(staff=staff, day=now.date())
        entry_record.entry = now.time()
        entry_record.save()
        return Response('ورود با موفقیت ثبت شد', status=status.HTTP_201_CREATED)


class ExitAPIView(CreateAPIView):
    """
        this endpoint is used to create a new Entry and need staff_id in request body
    """
    queryset = EntryAndExit.objects.prefetch_related('staff').all()
    serializer_class = EntryAndExitSerializer

    def create(self, request, *args, **kwargs):
        """
            hear we need staff_id in request body
        """
        staff_id = request.data.get('staff_id')
        now = timezone.now()

        try:
            staff = Staff.objects.get(id=staff_id)
        except Staff.DoesNotExist:
            return Response({'detail': 'کارمند یافت نشد'}, status=status.HTTP_404_NOT_FOUND)
        exit_record = EntryAndExit.objects.filter(staff=staff, day=now.date()).last()
        if not exit_record.is_checked_in():
            return Response('برای کارمند ورود ثبت نشده است', status=status.HTTP_400_BAD_REQUEST)
        if not exit_record.is_checked_out():
            exit_record.exit = now.time()
            exit_record.save()
            return Response('خروج با موفقیت ثبت شد', status=status.HTTP_201_CREATED)
        return Response('کاربر قبلا خارج شده است ', status=status.HTTP_400_BAD_REQUEST)
