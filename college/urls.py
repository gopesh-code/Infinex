from college import views
from django.urls import path
from . import views
from .views import UpdatePostView


urlpatterns = [
    path("", views.college, name="college"),
    path("notice/<int:myid>/", views.notice, name="notice"),
    path("application_form/", views.application_form, name="application_form"),
    path("edit_application/", views.edit_application, name="edit_application"),
    path("status/", views.status, name="status"),

    path("register/", views.register, name="register"),
    path("login/", views.loggedin, name="login"),

    path("handle_admin/", views.handle_admin, name="handle_admin"),
    path("users/", views.users, name="users"),
    path("student_application/<int:myid>/", views.student_application, name="student_application"),
    path("application_status/<int:pk>/", UpdatePostView.as_view(), name="application_status"),
    path("approved_applications/", views.approved_applications, name="approved_applications"),
    path("pending_applications/", views.pending_applications, name="pending_applications"),
    path("rejected_applications/", views.rejected_applications, name="rejected_applications"),
    path("logout/", views.loggedout, name="logout"),
    
]
