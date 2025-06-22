from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# Register viewsets for the five models that need full CRUD interaction
router.register(r'sector-subdivision-types', SectorSubdivisionTypeViewSet, basename='sector-subdivision-type')
router.register(r'subcities', SubcityViewSet, basename='subcity')
router.register(r'woredas', WoredaViewSet, basename='woreda')
router.register(r'organizational-units', OrganizationalUnitViewSet, basename='organizational-unit')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'employee-roles', EmployeeRoleViewSet, basename='employee-role')
router.register(r'subcity-subdivision-types', SubcitySubdivisionTypeViewSet, basename='subcity-subdivision-type')
router.register(r'divisions', DivisionViewSet, basename='division')

urlpatterns = [
    path('', include(router.urls)),
]
