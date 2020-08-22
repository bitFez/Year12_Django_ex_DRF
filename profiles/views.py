from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from . models import Profile
from reviews.models import Reviews
import requests, json, urllib
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import UserEditForm, ProfileEditForm
# Create your views here.
def profile_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    author = get_object_or_404(Profile, pk=pk)
    instagram = 'http://www.instagram.com/'
    insta_handle = urllib.parse.urljoin(instagram, author.insta)
    no_reviews = author.no_reviews
    reviews = Reviews.objects.filter(author=author.id)

    context = {'user':user, 'author':author, 'insta_handle':insta_handle, 'no_reviews':no_reviews, 'reviews':reviews}
    return render(request, 'profiles/profile_detail.html', context)

@login_required()
def edit_profile(request):
    author = get_object_or_404(Profile, pk=request.user.id)
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('edit_profile'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'author': author,
    }
    return render(request, 'profiles/edit_profile.html', context)
