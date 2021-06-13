from django.db import models

from ide_core.config import Config


class CodeFile(models.Model):
	# TODO: Please change this to use s3
	code_id = models.CharField(max_length=32)
	flag = models.BooleanField(default=False)

	source = models.TextField(max_length=Config.SOURCE_MAX_LIMIT)
	user_email = models.CharField(max_length=256)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
