from django.urls import path
from mobileApp import views

app_name = 'mobileApp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('create/',views.CreateProduct.as_view(),name='create'),
    path('update/<int:pk>/',views.UpdateProduct.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteProduct.as_view(),name='delete'),
]

