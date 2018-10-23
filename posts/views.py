from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import PostForm
from django.db.models import Q

from .models import Post


def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form= PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print(request.user)
		instance.user= request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
		
	else:
		pass


	#if request.method =="POST":
		
		#print type(request.POST)
		#print request.POST.get("content")
	context={"form":form}
	return render(request,"create.html",context)

	#if request.user is Post:
		#form=Post
		#if form._is valid:
	#context= {"form": form,}
	#return render(request, "create.html",context)
	#return render()

def post_details(request,id=None):
	instance=get_object_or_404(Post,id=id) 
	if instance.publish > timezone.now().date():
		context={"instance":instance,}
	#print(test)
	return render(request,"details.html",context)

	

def post_list(request):
	queryset_list=Post.objects.active()
	query=request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 10)
	page = request.GET.get('page')
	try:
		queryset_list =paginator.page(page) 
	except PageNotAnInteger:
		queryset_list=paginator.page(1)
	except EmptyPage:
		queryset_list=paginator.page(paginator.num_pages)

	context={"object_list":queryset_list,}
	

	return render(request,"list.html",context)

	

def post_update(request,id=None):
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context={"form":form,"instance":instance,}
	return render(request,"update.html",context)

def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("list")
	pass






# Create your views here.
