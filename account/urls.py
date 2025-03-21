from django.urls import path
from .views import user_login, dashboardview, logout_view

from django.contrib.auth.views import (LoginView,LogoutView, PasswordChangeView,PasswordResetView,
                                       PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,
                                       PasswordChangeDoneView)

urlpatterns=[
    # path('login/',user_login,name='login'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/',dashboardview, name='user_profile')
]