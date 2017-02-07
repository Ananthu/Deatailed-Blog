from django.http import HttpResponse 
from django.shortcuts import render,get_object_or_404,redirect
from models import Post
from forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
	context={ "form":form }
	return render(request,"my_blog/post_create.html",context)

def post_update(request,id=None):
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
	context={ "form":form,
			  "title":instance.title,
			  "instance":instance }

	return render(request,"my_blog/post_create.html",context)

def post_delete(request,id):
	form=PostForm(request.POST or None)
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("posts:index")

def index(request):
	lists=Post.objects.all().order_by("-timestamp")
	paginator = Paginator(lists, 10) # Show 25 lists per page
	page = request.GET.get('page')
	try:
		lists = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		lists = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		lists = paginator.page(paginator.num_pages)
	
	return render(request,"my_blog/index.html",{'lists':lists})

def detail(request,id):
	lists=Post.objects.get(pk=id)
	return render(request,"my_blog/detail.html",{'lists':lists})

