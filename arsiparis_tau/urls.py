from django.contrib import admin
from django.urls import path
from arsip import views  # Import fungsi dari app arsip yang barusan kita bikin

urlpatterns = [
    path('admin/', admin.site.urls),
    # Kosongin string awalnya ('') biar ini jadi halaman pertama (Home)
    path('', views.dashboard, name='dashboard'), 
]