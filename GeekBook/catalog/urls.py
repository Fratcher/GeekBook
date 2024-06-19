from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('year/<int:pk>', views.BookDetailView.as_view(), name='year-detail'),
    path('month/<int:pk>', views.MonthDetailView.as_view(), name = 'month-detail')
]


