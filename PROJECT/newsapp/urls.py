from django.urls import path
from newsapp.views import *

from .views import add_news
from newsapp.views import favorite_news
from .views import delete_news


urlpatterns = [
    # render html
    path('', index,name='index'),
    path('addnews',add_news,name='addnews'),
    path('favorite', favorite_news, name='favorite_news'),
    path('dashboard',dashboard,name='dashboard'),
    path('delete/<int:news_id>/', delete_news, name='delete_news'),
    

]