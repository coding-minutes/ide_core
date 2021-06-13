# from rest_framework import serializers
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import CodeFile
import random
import base64


class PingPongView(APIView):
    def get(self, request):
        return Response({"message": "pong"})


class SaveCode(APIView):
	def generate_id(self):
		"""generates a random id for the code of length (4,6)"""
		id_len = random.randint(4, 6)
		num = "".join([ str(random.randint(1, 9)) for i in range(id_len)])
		return num
	
	def post(self, request):
		# generate code_id
		code_id = self.generate_id()

		#generate a new code_id if already existed.
		while(len(CodeFile.objects.filter(code_id=code_id))):
			code_id = self.generate_id()


		# extract data from the params.
		source = request.POST['source']
		user_email = request.POST['user_email']
		flag = request.POST['flag']

		# base64 encoding of code.
		source = base64.b64encode(bytes(source, 'utf-8'))

		# create CodeFile object and save to DB.
		try:
			code = CodeFile(code_id = code_id, flag=flag, source=source, user_email=user_email)
			code.save()
			# print("code saved")
		except Exception as e:
			print("Somthing Wrong!", e)
		

		return Response({
			"status"  : "201",
			"message" : "code saved successfully",
			"code_id" : code_id
			}, content_type="application/json")



	def get(self, request):
		"""Get all the Codes"""
		
		all_codes = CodeFile.objects.all()
		
		all_codes_json = serializers.serialize('json', all_codes)
		

		return Response({
			"status" : 200,
			"codes" : all_codes_json
			})



	def delete(self, request):
		"""Delete All Codes"""

		CodeFile.objects.all().delete()

		return Response({
			"status" :"All deleted"
			})



class GetCode(APIView):
	def get(self, request, code_id):
		"""Get one code corresponding to its code_id if flag=True"""


		code = CodeFile.objects.filter(code_id=code_id, flag=True)
		code_json = serializers.serialize('json', code)

		if(len(code)):
			# if code exists
			return Response({
				"status": 200,
				"code_id" : code_id,
				"data" : code_json
				}, content_type = "application/json")
		else:
			# either id is wrong or flag=False
			return Response({
				"status": 200,
				"code_id" : code_id,
				"data" : "Code not available"
				}, content_type = "application/json")

