from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_router_v1 = DefaultRouter()
api_router_v1.register(r'posts', PostViewSet)
api_router_v1.register(r'groups', GroupViewSet)
api_router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                       CommentViewSet, basename='comment')
api_router_v1.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(api_router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/jwt/create/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'),

]
