from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('', views.home, name="home"),
	path('adminpanel/', views.register, name="adminpanel"),
    path('change-password/<int:user_id>/', views.change_password, name='change-password'),
	path('preview/', views.preview, name="preview"),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('form/', views.saveTimes, name="saveTimes"),
    path('my-reports/<int:employee_id>/', views.my_reports, name='my-reports'),
    path('time-archive/<int:entry_id>/', views.show_dtr_archive, name='time-archive'),
    path('deactivate-user/<int:user_id>/', views.deactivate_user, name='deactivate-user'),
    path('activate-user/<int:user_id>/', views.activate_user, name='activate-user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),
    path('adminpanel/search', views.searchBar, name='searchBar'),
    path('event/', views.holiday, name='holiday'),
    path('make-up/', views.make_up_class, name='make-up')
]

