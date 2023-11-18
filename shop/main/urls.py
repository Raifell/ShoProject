from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('category/<str:category>/', views.category_page, name='category'),
    path('category/<str:category>/<slug:p_slug>/', views.product_info, name='product')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
