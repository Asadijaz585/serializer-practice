from django.urls import path
from snippets import views
from snippets.views import filter_list

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('^snippets/(?P<user>.+)/$', filter_list.as_view()),
]