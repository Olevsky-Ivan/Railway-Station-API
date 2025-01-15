from user.views import CreateUserView, ManageUserView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
    path("login/", views.obtain_auth_token, name="token"),
]
