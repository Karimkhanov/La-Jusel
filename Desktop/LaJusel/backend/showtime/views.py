from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import showtimes
from .serializers import showtimesSerializer


@api_view(['GET'])
def show_list(request):
    if request.method == 'GET':
        showList = showtimes.objects.all()
        serializer = showtimesSerializer(showList, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def show_add(request):
    serializer = showtimesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_show_detail(request, pk=None):
    try:
        showList = showtimes.objects.get(id=pk)
    except showtimes.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = showtimesSerializer(showList)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = showtimesSerializer(
            instance=showList,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()  # update table
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        showList.delete()
        return Response({"deleted": True}, status=status.HTTP_204_NO_CONTENT)
