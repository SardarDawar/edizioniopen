from django.shortcuts import render
from .models import follow,post,message
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/loggin')
def profile_page(request):
    template = 'profile.html'
    objs = follow.objects.all()
    followers = 0
    following = 0
    for i in objs:
        if i.user == request.user.username:
            followers += 1
        if i.follower == request.user.username:
            following += 1
    objs = post.objects.all()
    posts = 0
    for i in objs:
        if i.posted_by == request.user.username:
            posts += 1
    objs = message.objects.all()
    messages = 0
    for i in objs:
        if i.reciever == request.user.username:
            messages += 1
    context = {'followers':followers,'following':following,'posts':posts,'messages':messages}
    return render(request,template,context)