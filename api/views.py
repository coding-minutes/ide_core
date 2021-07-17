from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from api.models import CodeFile
from api.serializers.base import BaseModelSerializer
from rest_framework import serializers
from utils.id_codec import get_id_codec

IdCodec = get_id_codec()


class CodeFileSerializer(BaseModelSerializer):
    id = serializers.SerializerMethodField(source="pk")

    class Meta:
        model = CodeFile
        fields = ["source", "user_email", "input", "lang", "id"]

    def get_id(self, obj):
        # Base 10 to 26
        # Encoding
        return IdCodec.convertIntToString(int(obj.pk))


class CodeFileDetailsView(RetrieveAPIView):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer

    def dispatch(self, request, *args, **kwargs):
        # Base 26 to 10
        # Decoding
        pk = kwargs.pop("pk")
        kwargs["pk"] = IdCodec.convertStringToInt(pk)
        return super().dispatch(request, *args, **kwargs)


class UpsertView(APIView):
    def post(self, request):
        body = request.data
        if body.get("id"):
            body["id"] = IdCodec.convertStringToInt(body["id"])
        codefile, created = CodeFile.objects.update_or_create(
            id=body.get("id"), defaults=body
        )

        serializer = CodeFileSerializer(codefile)

        if created:
            status = 201
        else:
            status = 200

        return Response(serializer.data, status=status)
