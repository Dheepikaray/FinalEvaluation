from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from new_app.models import blog
from new_app.serializers import BlogSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def list(request):
    if request.method == 'GET':
        studentset = blog.objects.all()
        serializer = BlogSerializer(studentset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def record(request, id):
    try:
        stud = blog.objects.get(id=id)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(stud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)
