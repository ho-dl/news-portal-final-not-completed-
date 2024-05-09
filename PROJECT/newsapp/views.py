from django.shortcuts import render ,redirect
from .models import News
from .models import FavoriteNews
from .models import News

# Create your views here.


def index(request):
    all_news = News.objects.all()
    user= request.user
    return render(request, 'index.html', {'all_news': all_news, 'user':user})


from .models import News

def add_news(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        images = request.FILES.get('images')

        news = News(heading=heading, content=content, images=images)
        news.save()

        # Check if user is logged in
        if request.user.is_authenticated:
            # Get or create favorite news object for the user
            favorite_news, created = FavoriteNews.objects.get_or_create(user=request.user)
            # Add the newly created news to the user's favorite list
            favorite_news.news.add(news)

        return redirect('dashboard')  # Redirect to news list in admin panel
    
    return render(request, 'add_news.html')





def favorite_news(request):
    if request.user.is_authenticated:
        favorite_news = FavoriteNews.objects.filter(user=request.user)
        if request.method == 'POST':
            news_id = request.POST.get('news_id')
            news = News.objects.get(pk=news_id)
            favorite_news_obj, created = FavoriteNews.objects.get_or_create(user=request.user)
            favorite_news_obj.news.add(news)
        return render(request, 'favorite_news.html', {'favorite_news': favorite_news})
    else:
        # Handle case where user is not logged in
        # Redirect to login page or display a message
        return redirect('login')
    # ok how set url of favorite_news.html

def dashboard(request):
    all_news = News.objects.all()
    return render(request, 'dashboard.html', {'all_news': all_news})



def delete_news(request, news_id):
    # Get the news object
    news = News.objects.get(pk=news_id)
    # Delete the news
    news.delete()
    return redirect('index')  # Redirect to the index page after deletion