
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from SN.views import *
from django.contrib.auth import views as auth_views
from SocialNetwork import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='SN/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('',post_view, name='home'),
    path('accounts/profile/',profile,name='profile'),
    path('post/add',post_add_view, name='post-add'),
    path('user/<str:username>/', user_profile, name='user_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)