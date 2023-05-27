
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, HOD_views, professor_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #login path
    path('', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),

    #this is hod panel
    path('HOD/home', HOD_views.HOME,name='hod_home'),
    path('HOD/Student/Add',HOD_views.ADD_STUDENTS,name='add_student'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
