from django.contrib import admin
from .models import Post
class postmodelAdmin(admin.ModelAdmin):
	list_display=['title','content','updated']
	#fields=['title','content']
	#readonly_field=['author_name']
	class Meta:
		model=Post
	

def author_name(self,obj,*args,**kwargs):
	
	return obj.title
admin.site.register(Post,postmodelAdmin)

# Register your models here.
