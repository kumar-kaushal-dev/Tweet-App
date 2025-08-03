from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import Http404
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm

def index(request):
    """
    Home page view
    """
    if request.user.is_authenticated:
        return redirect('tweet_list')
    return render(request, 'index.html')

@login_required
def tweet_list(request):
    """
    Display paginated list of all tweets
    """
    tweets = Tweet.objects.select_related('user').all()
    paginator = Paginator(tweets, 10)  # Show 10 tweets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_tweets': tweets.count()
    }
    return render(request, 'tweet_list.html', context)

@login_required
def tweet_create(request):
    """
    Create a new tweet
    """
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, 'Tweet posted successfully!')
            return redirect('tweet_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form, 'action': 'Create'})

@login_required
def tweet_edit(request, tweet_id):
    """
    Edit an existing tweet (only by the owner)
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    # Check if user owns the tweet
    if tweet.user != request.user:
        messages.error(request, 'You can only edit your own tweets.')
        return redirect('tweet_list')
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tweet updated successfully!')
            return redirect('tweet_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet_form.html', {
        'form': form, 
        'tweet': tweet, 
        'action': 'Edit'
    })

@login_required
def tweet_delete(request, tweet_id):
    """
    Delete a tweet (only by the owner)
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    # Check if user owns the tweet
    if tweet.user != request.user:
        messages.error(request, 'You can only delete your own tweets.')
        return redirect('tweet_list')
    
    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted successfully!')
        return redirect('tweet_list')
    
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    """
    User registration view
    """
    if request.user.is_authenticated:
        return redirect('tweet_list')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}! You are now logged in.')
            login(request, user)
            return redirect('tweet_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})