from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.AddView.as_view(),name='add_ts'),
    path('show/', views.ShowView.as_view(), name='list_ts'),
    path('del/<int:pk>/',views.Delete.as_view(),name='del_ts'),
    path('upd/<int:pk>/',views.Update.as_view(),name='upd_ts')
]