from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.dashboard_view,name='dashboard'),
    # path('search/', views.dashboard_view, name='search'),
    path('blog/<int:pk>/',views.blog,name='blog'),
    path('create_blog/',views.create_blog,name='create'), 
    path('create_cmt/<int:pk>/',views.create_cmt,name='create_cmt'),
    path('edit_cmt/<int:pk>/<int:pk1>/',views.edit_cmt,name='edit_cmt'),
    path('delete_cmt/<int:pk>/<int:pk1>/',views.delete_cmt,name='delete_cmt'),

    path('custom_tag/',create_tag,name='custom_tag')

]