from django.conf import settings
from django.conf.urls.static import static
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.Home , name='home'),
    path('blog/', views.Blog , name='blog'),
    path('<slug:post_slug>', views.Single_post, name='single'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('category/<slug:category_slug>', views.category_details, name = 'category_details'  ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)