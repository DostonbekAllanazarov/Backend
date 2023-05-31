from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('question', views.question, name="question"),
    path('room/<int:id>/', views.answer, name="room"),
    path('signup', views.signup, name="signup"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
