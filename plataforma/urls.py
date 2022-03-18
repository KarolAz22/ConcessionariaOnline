from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('veiculo/<str:id>', views.veiculo, name="veiculo"),
    path('anuncie/', views.anuncie,name='anuncie'),
    path('search/', views.pesquisar, name='pesquisa'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)