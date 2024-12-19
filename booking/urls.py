from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, ParentViewSet, SubjectViewSet, PaymentViewSet, EventViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename="school")
router.register(r'students', StudentViewSet, basename="student")
router.register(r'parents', ParentViewSet, basename="parent")
router.register(r'subjects', SubjectViewSet, basename="subject")
router.register(r'payments', PaymentViewSet, basename="payment")
router.register(r'events', EventViewSet, basename="event")

urlpatterns = [
    path('api/', include(router.urls)),
]
