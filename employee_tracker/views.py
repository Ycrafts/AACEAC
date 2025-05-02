from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to specify the page size via the URL
    max_page_size = 100  # Set a limit for the maximum page size


class SectorSubdivisionTypeViewSet(viewsets.ModelViewSet):
    queryset = SectorSubdivisionType.objects.all().order_by('name')
    serializer_class = SectorSubdivisionTypeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['name'] 

class SubcityViewSet(viewsets.ModelViewSet):
    queryset = Subcity.objects.all().order_by('name')
    serializer_class = SubcitySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ['name'] 

class WoredaViewSet(viewsets.ModelViewSet):
    queryset = Woreda.objects.all().order_by('name')
    serializer_class = WoredaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ['name', 'subcity__name'] 

class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    queryset = OrganizationalUnit.objects.select_related(
        'division', 'sector_subdiv_type', 'subcity_subdiv_type',
        'parent', 'subcity', 'woreda'
    )
    serializer_class = OrganizationalUnitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ['name', 'division__name','sector_subdiv_type__name','subcity__name','woreda__name'] 

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('organizationalunit', 'role')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = [
        'fname',
        'mname',
        'lname',
        'organizational_unit__name',
        'organizational_unit__sector_subdiv_type__name',
        'organizational_unit__woreda__name',
        'organizational_unit__subcity__name',
        'organizational_unit__role__name'
    ]

class EmployeeRoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer
    permission_classes = [IsAuthenticated]

class SubcitySubdivisionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubcitySubdivisionType.objects.all()
    serializer_class = SubcitySubdivisionTypeSerializer
    permission_classes = [IsAuthenticated]

class DivisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [IsAuthenticated]
