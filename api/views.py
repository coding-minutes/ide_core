from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from api.models import CodeFile
from api.serializers.base import BaseModelSerializer


class CodeFileSerializer(BaseModelSerializer):
    class Meta:
        model = CodeFile
        fields = ["source", "user_email", "input", "lang", "id"]
        read_only_fields = ["id"]


class CodeFileDetailsView(RetrieveAPIView):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer


class UpsertView(APIView):
    def post(self, request):
        body = request.data
        id = body.get("id", None)
        codefile, created = CodeFile.objects.update_or_create(id=id, defaults=body)

        serializer = CodeFileSerializer(codefile)

        if created:
            status = 201
        else:
            status = 200

        return Response(
            {"data": serializer.data["data"], "created": created}, status=status
        )
