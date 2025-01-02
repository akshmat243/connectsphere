from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', index_view, name='index'),    
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('post/', post_view, name='post'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('settings/', settings_view, name='settings'),
    path('editprofile/', edit_profile_view, name='editprofile'),
    path('profile/<str:username>', profile_view, name='profile'),
    path('delete_post/<int:pk>', delete_post_view, name='delete_post'),
    path('edit_post/<int:pk>', edit_post_view, name='edit_post'),
    path('likes/<int:post_id>', likes_view, name='likes'),
    path('comment/', comment_view, name='comment'),
    
    
    
    # when user logged in.
    path('password_change/', PasswordChangeView.as_view(template_name="change/password_change_form.html"), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name="change/password_change_done.html"), name='password_change_done'),
    
    # when user forgot password
    path('password_reset/', PasswordResetView.as_view(template_name="change/password_reset.html"), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name="change/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="change/set_new_password.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="change/password_reset_complete.html"), name='password_reset_complete'),
    
]

# https://www.youtube.com/embed/csqBMqvW17Y?si=8vm8bbxAJ8Wl2rA6

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)