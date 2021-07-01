from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from api.models import CodeFile
from api.serializers.base import BaseModelSerializer


class CodeFileSerializer(BaseModelSerializer):
    class Meta:
        model = CodeFile
        fields = ["source", "user_email", "input", "lang", "id"]
        read_only_fields = ["id"]

class PingPongView(APIView):
    def get(self, request):
        return Response({"message" : "pong"})

class CodeFileDetailsView(RetrieveUpdateAPIView):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer


class CodeFileCreateView(CreateAPIView):
    serializer_class = CodeFileSerializer
