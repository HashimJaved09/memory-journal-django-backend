from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.http import HttpResponseRedirect

from accounts.models import User
from accounts.serializers import UserSerializer, UsersSerializer, UserEditSerializer


# class UserCreate(APIView, LoginRequiredMixin):
class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    """
    Creates the user.
    """
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    """
    Creates the user.
    """
    serializer_class = UsersSerializer

    def get(self, request, format='json'):
        users = User.objects.all()
        return Response(self.serializer_class(users, many=True).data, status=status.HTTP_200_OK)


class UserEditView(APIView):
    """
    Creates the user.
    """
    serializer_class = UserEditSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)