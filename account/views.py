from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterView(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        summary="Create a super user",
        description="this api use to create a super user",
        responses={200: serializer_class(many=True)},
    )
    def post(self, request):
        ser_data = self.serializer_class(data=request.data)
        if not ser_data.is_valid():
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        user = ser_data.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
            'message': 'ثبت ‌نام با موفقیت انجام شد.',
            'refresh': str(refresh),
            'access': access_token,
        }, status=status.HTTP_201_CREATED)

        response['Authorization'] = f'Bearer {access_token}'
        response['X-Refresh-Token'] = str(refresh)
        return response


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @extend_schema(
        summary="Login a user",
        description="this api use to login a user",
        responses={200: serializer_class(many=True)},
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            'refresh': serializer.validated_data['refresh'],
            'access': serializer.validated_data['access'],
        })
