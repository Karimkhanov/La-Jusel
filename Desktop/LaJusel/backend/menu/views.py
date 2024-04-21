from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu
from .serializers import MenuSerializer


class MenuView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailView(APIView):
    def get_object(self, pk=None):
        try:
            menu = Menu.objects.get(id=pk)
            return menu
        except Menu.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, pk=None):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        menu = self.get_object(pk)
        menu.delete()
        return Response({"deleted": True}, status=status.HTTP_204_NO_CONTENT)
