from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views



from . import views
appname = "accounts"
urlpatterns = [



    path('profile', views.profile.as_view(), name="profile"),
    path('document/', views.document, name="document"),
    path('signup/', views.signup, name="signup"),
    path('pdf/', views.pdfedit, name="pdf"),
    path('renderPdf/',  views.renderPdf, name="renderPdf"),

    #login path

    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]