from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class fileupload(models.Model):
	
	filesize = models.CharField(max_length=50,null=True,blank=True)
	url      = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(allowed_extensions=['wav'])])
	text_url = models.CharField(max_length=256, null=True, blank=True)
	updated_url = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		return self.filesize