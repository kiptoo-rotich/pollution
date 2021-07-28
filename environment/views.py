from django.shortcuts import render,redirect
from .models import Post,Response,Cleanup,Reactions
from .forms import PolutionForm,ResponseForm,CleanupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    cases=Post.objects.all()
    return render(request,'main/index.html',{'cases':cases})

@login_required(login_url='/accounts/login/')
def newPost(request):
    current_user=request.user
    
    if request.method=="POST":
        form=PolutionForm(request.POST,request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.user=request.user
            new_post.save()
        
            return redirect('index')
    else:
        form=PolutionForm()
    return render(request,'main/add_post.html', {'form':form})

@login_required(login_url='/accounts/login/')
def Reactions_view(request,id):
    post=Post.objects.get(id=id)
    responses=Response.objects.filter(post_id=id)
    user=request.user
    if request.method=="POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            reactions=form.save(commit=False)
            reactions.post_id=post
            reactions.user=user
            reactions.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form=ResponseForm()
    return render(request,'main/reactions.html',{'form':form,'responses':responses,'post':post})

@login_required(login_url='/accounts/login/')
def cleanup(request):
    current_user=request.user
    if request.method =='POST':
        form=CleanupForm(request.POST,request.FILES)
        if form.is_valid():
            new_cleanup=form.save(commit=False)
            new_cleanup.user=current_user
            new_cleanup.save()
            
            return redirect('events')
    else:
        form=CleanupForm()
    return render(request,'main/cleanup.html',{'form':form})

@login_required(login_url='/accounts/login/')
def cleanupquery(request):
    clean=Cleanup.objects.all()
    return render(request,'main/events.html',{'clean':clean})

@login_required(login_url='/accounts/login/')
def Cleanup_reviews(request,id):
    post=Cleanup.objects.get(id=id)
    responses=Reactions.objects.filter(clean_id=id)
    user=request.user
    if request.method=="POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            reactions=form.save(commit=False)
            reactions.post_id=post
            reactions.user=user
            reactions.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form=ResponseForm()
    return render(request,'main/cleanup_reviews.html',{'form':form,'responses':responses,'post':post})