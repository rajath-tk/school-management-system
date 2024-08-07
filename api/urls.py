# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, TeacherViewSet, NonTeachingStaffViewSet, SubjectViewSet, EnrollmentViewSet, AttendanceViewSet, ExamViewSet, ExamResultViewSet, RoomViewSet, TimetableViewSet, EventViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet)
router.register(r'non_teaching_staff', NonTeachingStaffViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam_results', ExamResultViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'events', EventViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
