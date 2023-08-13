from django.urls import path, include 

import user.views as views 

urlpatterns = [
    path("", views.LandingPage.as_view(), name="landing_page")
]