from django.urls import path

from new_app import views, api_views

urlpatterns = [
path('', views.new, name='new'),
    path('base/', views.base, name='base'),
    path('publishers/', views.publishers, name='publishers'),
    path('customers/', views.customers, name='customers'),
    path('login1', views.login_view, name='login1'),
    path('register/', views.publisher_register, name='register'),
    path('register2/', views.customer_register, name='register2'),
    path('view/', views.view, name='view'),
    path('view1/', views.view1, name='view1'),
    path('delt/<int:id>/', views.delete, name='delt'),
    path('update1/<int:id>/', views.update, name='update1'),
    path('register3',views.blog_register, name='register3'),
    path('view2',views.view2, name='view2'),
    path('update2/<int:id>/', views.blogupdate, name='update2'),
    path('userblog', views.view_blog_user, name='userblog'),
    path('delete1/<int:id>/', views.delete1, name='delete1'),


    path('list', api_views.list, name='list'),
    path('record/<int:id>/', api_views.record, name='record')


]
