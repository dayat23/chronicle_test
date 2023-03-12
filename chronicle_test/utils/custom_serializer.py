from dj_rest_auth.registration.serializers import (
    RegisterSerializer as BaseRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(
    exclude_fields=("username",),
)
class CustomLoginSerializer(BaseLoginSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})


@extend_schema_serializer(
    exclude_fields=("username",),
)
class CustomRegisterSerializer(BaseRegisterSerializer):
    pass
