from django.db import models

# Create your models here.
class Images(models.Model):
	title = models.CharField(max_length=200)
	img_data = models.TextField()
   
    	def __unicode__(self):
        	return self.title
