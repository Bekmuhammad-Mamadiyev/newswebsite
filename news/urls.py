from unicodedata import category

from django.urls import path
from .views import (news_list, contactpageview, categorypageview, HomePageView, newsdetailview,
                    LocalPageView, WorldPageView, FanTexnikaPageView, SportPageView)

urlpatterns = [
    path('news/',news_list, name='newslists'),
    path("", HomePageView.as_view(), name='home_page'),
    path("contact/", contactpageview, name='contact_page'),
    path('category/',categorypageview, name='category_page'),
    path('news/local/', LocalPageView.as_view(), name='news_local_page'),
    path('news/world/', WorldPageView.as_view(), name='news_world_page'),
    path('news/fan/', FanTexnikaPageView.as_view(), name='news_fan_page'),
    path('news/sport/', SportPageView.as_view(), name='news_sport_page'),
    path('news/<slug:news>/', newsdetailview, name='news_detail_page'),

]