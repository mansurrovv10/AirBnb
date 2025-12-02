from django.urls import path,include
from .views import (UserProfileListAPIView,UserProfileDetailAPIView,CityListAPIView,
                    PropertyListAPIView,PropertyDetailAPIView,CityDetailAPIView,
                    BookingViewSet,ReviewCreateAPIView,ReviewEditAPIView,PropertyViewSet,
                    RegisterCreateView, LoginView,LogoutView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'booking', BookingViewSet)
router.register(r'property_create',PropertyViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view(), name='property-list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
    path('city/', CityListAPIView.as_view(), name='city-list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city-detail'),
    path('userprofile/', UserProfileListAPIView.as_view(), name='user-profile-list'),
    path('userprofile/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user-profile-detail'),
    path('review/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewEditAPIView.as_view(), name='review-edit'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
