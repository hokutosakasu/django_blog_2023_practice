from django .urls import path
from .import views
from markdownx.models import MarkdownxField

urlpatterns = [
    path('', views.index,name='index'),
    # path('list',views.PostListView.as_view(),name='list'),
    path('detail/<int:pk>',views.PostListDetailView.as_view(),name='detail'),
    # path('category/<str:category>',views.CategoryView.as_view(),name='category'),
    path('category/<str:category>/', views.CategoryView.as_view(),name='category'),
    path('serach', views.SearchView.as_view(),name='serach'),
    #  path('category/<str:category>',views.category,name='category'),

    
]