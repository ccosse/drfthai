from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from thai import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('phrases/',
        views.PhraseList.as_view(),
        name='phrase-list'),
    path('phrases/<int:pk>/',
        views.PhraseDetail.as_view(),
        name='phrase-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),

    path('expander/',
        views.expander,
        name='expander'),
])
