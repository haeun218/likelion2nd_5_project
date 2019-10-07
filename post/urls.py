# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework -> router -> url

router = DefaultRouter() # -> ? API ROOT 없어 ?
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.PostList.as_view()), # 그냥 뭐라도 메인에 뜨라고 넣음.
    # path('post/', views.PostList.as_view()),
    # path('post/<int:pk>/', views.PostDetail.as_view()),
]