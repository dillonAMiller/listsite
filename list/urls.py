from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Checklist_id>/', views.listIndex, name='listIndex'),
    path('<int:Checklist_id>/<int:Set_id>/', views.setDetail, name='SetDetail'),
    path('<int:Checklist_id>/<int:Set_id>/<int:Item_id>/', views.itemDetail, name='ItemDetail')
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:Checklist_id>/', views.DetailView.as_view(), name='detail'),
    
]