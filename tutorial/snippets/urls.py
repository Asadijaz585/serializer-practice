from django.urls import path
from snippets import views
from snippets.views import filterList

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/filter/', filterList.as_view()), # http://127.0.0.1:8000/snippets/filter/?id=1
]