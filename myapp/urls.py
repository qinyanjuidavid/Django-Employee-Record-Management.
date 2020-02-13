from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
app_name='myapp'
urlpatterns=[
path('',views.Employee_list,name='list'),
path('details/employee/<id>/',views.Employee_details,name="details"),
path('employee/form/',views.Employee_form,name="emp_form"),
path('employee/update/<id>/',views.Employee_update,name="update"),
path('employee/delete/<id>/',views.Employee_delete,name='delete'),
path('login/',auth_views.LoginView.as_view(template_name="myapp/login.html"),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name="myapp/logout.html"),name="logout")
]
