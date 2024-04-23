from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSignUpSerializer


# Create your views here.
class UserSignUpAPIView(APIView):
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
