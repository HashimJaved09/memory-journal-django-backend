from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Memory
from .serializers import MemorySerializer


class GlobalMemoryView(APIView):
    serializer_class = MemorySerializer
    model_class = Memory

    def get_objects(self):
        return self.model_class.objects.filter(is_active=True)

    def get(self, request, format=None):
        serializer = self.serializer_class(self.get_objects(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MemoryView(APIView):
    serializer_class = MemorySerializer
    model_class = Memory

    def post(self, request, format='json'):
        dict_data = request.data
        dict_data['user'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_objects(self, request):
        return self.model_class.objects.filter(user=request.user, is_active=True)

    def get(self, request, format=None):
        serializer = self.serializer_class(self.get_objects(request), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MemoryEditView(APIView):
    serializer_class = MemorySerializer
    model_class = Memory

    def get_object(self, id, request):
        try:
            return self.model_class.objects.get(id=id, user=request.user)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk, request))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        dict_data = request.data
        dict_data['user'] = request.user.id
        user = self.get_object(pk, request)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk, request)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)