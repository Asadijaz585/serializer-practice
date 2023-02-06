from django.urls import path
from snippets import views
from snippets.views import filter_list, search

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('', filter_list.as_view()),
    path('snippets/<str:pk>/', search.as_view())
]