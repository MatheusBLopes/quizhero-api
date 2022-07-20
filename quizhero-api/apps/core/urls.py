from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.core.views import ChangePasswordView, RegisterView, UpdateProfileView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("change_password/", ChangePasswordView.as_view(), name="auth_change_password"),
    path("update_profile/", UpdateProfileView.as_view(), name="auth_update_profile"),
]
