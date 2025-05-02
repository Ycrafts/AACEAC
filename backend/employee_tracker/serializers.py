from rest_framework import serializers
from .models import *

class SectorSubdivisionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorSubdivisionType
        fields = ['id', 'name']


class SubcitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcity
        fields = ['id', 'name']


class WoredaSerializer(serializers.ModelSerializer):
    subcity_name = serializers.CharField(source='subcity.name')

    class Meta:
        model = Woreda
        fields = ['id', 'name', 'subcity', 'subcity_name']


class OrganizationalUnitSerializer(serializers.ModelSerializer):
    division_name = serializers.CharField(source='division.name', read_only=True)
    sector_subdiv_type_name = serializers.CharField(source='sector_subdiv_type.name')
    subcity_subdiv_type_name = serializers.CharField(source='subcity_subdiv_type.name')
    subcity_name = serializers.CharField(source='subcity.name')
    woreda_name = serializers.CharField(source='woreda.name')
    parent_name = serializers.CharField(source='parent.name')

    class Meta:
        model = OrganizationalUnit
        fields = [
            'id', 'name', 'division', 'division_name',
            'required_employees_no', 'sector_subdiv_type', 'sector_subdiv_type_name',
            'subcity_subdiv_type', 'subcity_subdiv_type_name',
            'parent', 'parent_name',
            'subcity', 'subcity_name', 'woreda', 'woreda_name'
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    organizationalunit_name = serializers.CharField(source='organizationalunit.name')
    role_name = serializers.CharField(source='role.role')

    class Meta:
        model = Employee
        fields = [
            'id', 'fname', 'mname', 'lname', 'phone_no',
            'organizationalunit', 'organizationalunit_name',
            'role', 'role_name'
        ]

class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = ['id', 'role']
        read_only_fields = ['role'] 

class SubcitySubdivisionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcitySubdivisionType
        fields = ['id', 'name']
        read_only_fields = ['name']  

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['id', 'name']
        read_only_fields = ['name']  

