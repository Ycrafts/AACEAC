from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models.deletion import ProtectedError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class Pagination(PageNumberPagination):
    page_size = 10  # items per page
    page_size_query_param = 'page_size' 
    max_page_size = 100

class SectorSubdivisionTypeViewSet(viewsets.ModelViewSet):
    queryset = SectorSubdivisionType.objects.all().order_by('name')
    serializer_class = SectorSubdivisionTypeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['name'] 
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "This sector subdivision type cannot be deleted because it is referenced by other data (e.g., Woredas)."},
                status=status.HTTP_409_CONFLICT
            )

    
class SubcityViewSet(viewsets.ModelViewSet):
    queryset = Subcity.objects.all().order_by('name')
    serializer_class = SubcitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['name'] 
    
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "This subcity cannot be deleted because it is referenced by other data (e.g., Woredas)."},
                status=status.HTTP_409_CONFLICT
            )

class WoredaViewSet(viewsets.ModelViewSet):
    queryset = Woreda.objects.all().order_by('name')
    serializer_class = WoredaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ['name', 'subcity__name']

    @action(detail=False, methods=['get'])
    def all(self, request):
        # Bypass pagination for this endpoint
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "This organizational unit cannot be deleted because it is referenced by other data (e.g., other organizational units)."},
                status=status.HTTP_409_CONFLICT
            )

class EmployeeViewSet(viewsets.ModelViewSet):
    # Add nested relationships to select_related for efficiency
    queryset = Employee.objects.select_related(
        'organizationalunit',
        'organizationalunit__woreda', # Add woreda
        'organizationalunit__subcity', # Add subcity
        'organizationalunit__sector_subdiv_type', # Add sector subdivision type
        'organizationalunit__subcity_subdiv_type', # Add subcity subdivision type
        'organizationalunit__division', # Add division
        'organizationalunit__parent', # Add parent organizational unit
        'role'
    )
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = [
        'fname',
        'mname',
        'lname',
        'phone_no',
        'organizationalunit__name',
        'role__role', # Changed from role__name to role__role since that's the field name in the Role model

        # Add fields from the related OrganizationalUnit's relationships
        'organizationalunit__woreda__name', # Assuming Woreda model has a 'name' field
        'organizationalunit__subcity__name', # Assuming Subcity model has a 'name' field
        'organizationalunit__sector_subdiv_type__name', # Assuming SectorSubdivisionType has a 'name' field
        'organizationalunit__division__name', # Assuming Division model has a 'name' field
        'organizationalunit__parent__name', # Assuming OrganizationalUnit has a 'name' field for the parent
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
