from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer, UserUpdateSerializer

User = get_user_model()


class UserViewSet(ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_staff=False)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return UserUpdateSerializer
        return UserDetailsSerializer

    def get_object(self):
        return self.request.user


user_delete_view_api = UserDetailView.as_view()
