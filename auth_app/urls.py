from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.dashboard_view,name='dashboard'),
    path('blog/<int:pk>/',views.blog,name='blog'),
    path('search/',views.search,name='search'), 
    path('create_blog/',views.blog,name='create'), 
    path('create_cmt/<int:pk>/',views.create_cmt,name='create_cmt'),
    path('edit_cmt/<int:pk>/<int:pk1>/',views.edit_cmt,name='edit_cmt'),
    path('delete_cmt/<int:pk>/<int:pk1>/',views.delete_cmt,name='delete_cmt'),

]