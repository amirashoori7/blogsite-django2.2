from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #post views
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.contact_us, name='contact_us'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/',
         views.index, name='index')
]
