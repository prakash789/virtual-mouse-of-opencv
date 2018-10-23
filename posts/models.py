#from __future__ import unicode_literals
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
#from django.utils.encoding import iri_to_uri
from django.utils import timezone

class PostManager(models.Manager):
	def active(self,*args,**kwargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())


class Post(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title=models.CharField(max_length=120)
    image = models.ImageField( 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content=models.TextField()
    draft=models.BooleanField(default=False)
    publish=models.DateField(auto_now=False,auto_now_add=False)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    objects= PostManager()


    def __unicode__(self):
		return self.title
    def __str__(self):
        return self.title


    def get_absolute_url(self):
		return reverse ("details", kwargs={"id":self.id})

    class Meta:
		ordering=["-timestamp"]
		#return "/posts/detail-s/%s/" %(self.id)



# Create your models here.
