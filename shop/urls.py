from tkinter.font import names
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterViewSet.as_view(), name = 'register'),
    path('login/', CustomLoginViewSet.as_view(), name = 'login'),
    path('logout/', LogoutViewSet.as_view(), name = 'logout'),


    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'product_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'user_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'category_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'rating_detail'),

    path('product_photos/', ProductPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'product_photos_list'),
    path('product_photos/<int:pk>/', ProductPhotosViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'product_photos_detail'),

    path('reviews/', ReviewsViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'reviews_list'),
    path('reviews/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'reviews_detail'),

]


