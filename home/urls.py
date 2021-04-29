from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('', views.index),
   path('contact/', views.contact),
   path('game1/', views.game1),
   path('game2/', views.game2),
   path('game3/', views.game3),
   path('game4/', views.game4),
   path('game5/', views.game5),
   path('game6/', views.game6),
   path('game7/', views.game7),
   path('game8/', views.game8),
   path('game9/', views.game9),
   path('game10/', views.game10),
   path('about2048/', views.about2048),
   path('aboutAstray/', views.aboutAstray),
   path('aboutBomb/', views.aboutBomb),
   path('aboutFlappybird/', views.aboutFlappybird),
   path('aboutHexGL/', views.aboutHexGL),
   path('aboutHextris/', views.aboutHextris),
   path('aboutMario/', views.aboutMario),
   path('aboutPuzzles/', views.aboutPuzzles),
   path('aboutSnake/', views.aboutSnake),
   path('aboutTrex/', views.aboutTrex),
   path('register/', views.register),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout')
   

]