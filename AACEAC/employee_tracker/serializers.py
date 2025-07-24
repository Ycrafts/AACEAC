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
    subcity_name = serializers.CharField(source='subcity.name', read_only=True)
    subcity = serializers.PrimaryKeyRelatedField(queryset=Subcity.objects.all())

    class Meta:
        model = Woreda
        fields = ['id', 'name', 'subcity', 'subcity_name']



class OrganizationalUnitSerializer(serializers.ModelSerializer):
 
    division_name = serializers.SerializerMethodField()
    sector_subdiv_type_name = serializers.SerializerMethodField()
    subcity_subdiv_type_name = serializers.SerializerMethodField()
    subcity_name = serializers.SerializerMethodField()
    woreda_name = serializers.SerializerMethodField()
    parent_name = serializers.SerializerMethodField() # Assuming 'parent' FK is nullable


    division = serializers.PrimaryKeyRelatedField(queryset=Division.objects.all(), allow_null=True, required=False)
    sector_subdiv_type = serializers.PrimaryKeyRelatedField(queryset=SectorSubdivisionType.objects.all(), allow_null=True, required=False)
    subcity_subdiv_type = serializers.PrimaryKeyRelatedField(queryset=SubcitySubdivisionType.objects.all(), allow_null=True, required=False)
    parent = serializers.PrimaryKeyRelatedField(queryset=OrganizationalUnit.objects.all(), allow_null=True, required=False) # Parent FK points to itself
    subcity = serializers.PrimaryKeyRelatedField(queryset=Subcity.objects.all(), allow_null=True, required=False)
    woreda = serializers.PrimaryKeyRelatedField(queryset=Woreda.objects.all(), allow_null=True, required=False)


    class Meta:
        model = OrganizationalUnit
        fields = [
            'id',
            'name',
            'required_employees_no', 

            'division',
            'sector_subdiv_type',
            'subcity_subdiv_type',
            'parent',
            'subcity',
            'woreda',

            'division_name',
            'sector_subdiv_type_name',
            'subcity_subdiv_type_name',
            'subcity_name',
            'woreda_name',
            'parent_name',

        ]

    def get_division_name(self, obj):
        """Returns the name of the division, or None if null."""
        if obj.division:
            return obj.division.name
        return None # Return None if the FK is null

    def get_sector_subdiv_type_name(self, obj):
        """Returns the name of the sector subdivision type, or None if null."""
        if obj.sector_subdiv_type:
            return obj.sector_subdiv_type.name
        return None

    def get_subcity_subdiv_type_name(self, obj):
        """Returns the name of the subcity subdivision type, or None if null."""
        if obj.subcity_subdiv_type:
            return obj.subcity_subdiv_type.name
        return None

    def get_subcity_name(self, obj):
        """Returns the name of the subcity, or None if null."""
        if obj.subcity:
            return obj.subcity.name
        return None

    def get_woreda_name(self, obj):
        """Returns the name of the woreda, or None if null."""
        if obj.woreda:
            return obj.woreda.name
        return None

    def get_parent_name(self, obj):
        """Returns the name of the parent organizational unit, or None if null."""
        if obj.parent:
            return obj.parent.name
        return None

class EmployeeSerializer(serializers.ModelSerializer):
    organizationalunit_name = serializers.CharField(source='organizationalunit.name', read_only=True)  # Add read_only=True
    role_name = serializers.CharField(source='role.role', read_only=True)  # Add read_only=True

    class Meta:
        model = Employee
        fields = [
            'id', 'fname', 'mname', 'lname', 'phone_no',
            'organizationalunit', 'organizationalunit_name',
            'role', 'role_name', 'status'
        ]
        read_only_fields = ['organizationalunit_name', 'role_name']  # Add this line

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

