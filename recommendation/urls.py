from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('developer/', views.developer, name='developer'),
    path('blog/', views.blog, name='blog'),
    # path('authentication/' , views.authentication , name='authentication'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
