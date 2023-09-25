from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('profile/<int:pk>/',views.profile,name='profile'),

    path('createpost/', views.createPost, name='createPost'),
    path('post/<int:pk>', views.post, name='post'),
    
    path('accounts/login/', views.login_view, name='login'),
    path('createaccount/', views.create_account, name='register'),
    path('logout/', views.logOut_view,name='logOut')
]