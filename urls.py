from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('authorized', views.authorized),
    path('weights' ,views.weightListView.as_view(), name="weights.list"),
    path('weights', views.weightCreateView.as_view(), name="weights.new"),
    path('weights/<int:pk>', views.weightDetailView.as_view(), name="weights.dtails"),
    path('login', views.loginauth.as_view()),
    path('logout', views.logoutauth.as_view()),
    path('signup', views.signup.as_view())
]