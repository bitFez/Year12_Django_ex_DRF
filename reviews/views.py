from django.shortcuts import render, get_object_or_404, redirect
from . models import Reviews
import requests, json, urllib
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Profile
from . forms import CreateUserForm, ReviewForm
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from .serializers import ReviewSerializer

# Create your views here.
def home(request):
    reviews=Reviews.objects
    reviewers=Profile.objects.filter(no_reviews__gte=1).order_by('-no_reviews')

    return render(request, 'reviews/home.html', {'reviews':reviews, 'reviewers':reviewers})

def filmreview(request, review_id):

    review_detail = get_object_or_404(Reviews, pk=review_id)
    review = Reviews.objects.get(id=review_id)
    title = review.title
    author = review.author
    pub_date = review.pub_date
    imdb_ref = review.imdb_ref
    body= review.body
    image = review.image
    apiurl = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"
    url = urllib.parse.urljoin(apiurl, imdb_ref)
    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "b385a20357msh7b3963623e55750p124c50jsnb26567f00801"
        }
    criticR = review.criticR
    applauds = review.applauds
    response = requests.request("GET", url, headers=headers).json()
    stars = (criticR*'⭐')
    rating = response['rating']
    votes = response['rating_votes']
    year = response['year']
    dura = response['length']
    plot = response['plot']



    context = {'review':review, 'title':title, 'author':author, 'pub_date':pub_date, 'image':image, 'imdb_ref':imdb_ref, 'body':body,
                'rating':rating, 'votes':votes, 'year':year, 'dura':dura, 'plot':plot, 'stars':stars, 'criticR':criticR, 'applauds':applauds}
    return render(request, 'reviews/filmreview.html', context)

def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(author=user)
            messages.success(request, 'Account created, now log in '+ username)
            return redirect('login')
        else:
            context = {'form':form}
            return render(request, 'registration/register.html', context)
    else:

        context = {'form':form}
        return render(request, 'registration/register.html', context)

@login_required
def submitreview(request):
    form = ReviewForm()
    author = get_object_or_404(Profile, pk=request.user.id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False) # dont save juts yet!
            review.author = request.user # attach author to the instance of the review
            author.no_reviews += 1
            review.save() # now save it with the author attached!
            author.save()
            return redirect('home')
        else:
            form = ReviewForm()
    return render(request, 'reviews/reviewform.html', {'form':form})


class ReviewsList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer