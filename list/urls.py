from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Checklist_id>/', views.detail, name='detail'),
    path('<int:Set_id>/', views.setDetail, name='SetDetail')
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:Checklist_id>/', views.DetailView.as_view(), name='detail'),
    
]