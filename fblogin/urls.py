from django.contrib import admin
from django.urls import path,include
from login import views as viewslogin
from profileinfo import views as viewsprofile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',viewslogin.status,name='home'),
    path('loggin',viewslogin.login,name='login'),
    path('logout',viewslogin.logout,name='logout'),
    path('signup',viewslogin.signup,name='signup'),
    path('changepass',viewslogin.changepass,name='changepass'),
    path('forgot',viewslogin.forgot,name='forgot'),
    path('profile',viewsprofile.profile_page,name='profile'),
    path('account/', include('allauth.urls'))
]
