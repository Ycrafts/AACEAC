from django.db import models
from django.forms import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError

class DuplicateEntryError(DjangoValidationError):
    """Custom error for duplicate entries"""
    def __init__(self, model_name, field_name, value):
        message = f"A {model_name} with the {field_name} '{value}' already exists. Please use a different {field_name}."
        super().__init__(message)

def validate_unique_case_insensitive(value, model_class, field_name, instance=None):
    """Validate that the value is unique case-insensitively"""
    lookup = {f"{field_name}__iexact": value}
    if instance and instance.pk:
        lookup['pk__ne'] = instance.pk
    
    if model_class.objects.filter(**lookup).exists():
        model_name = model_class.__name__.lower()
        raise DuplicateEntryError(model_name, field_name, value)

class Division(models.Model):
    class DivisionType(models.TextChoices):
        SECTOR_OFFICE = 'Sector Office', 'Sector Office'
        SUBCITY = 'Subcity', 'Subcity'
        COLLEGE = 'College', 'College'
        HOSPITAL = 'Hospital', 'Hospital'

    name = models.CharField(
        max_length=50,
        choices=DivisionType.choices
    )

    def __str__(self):
        return self.name

class SectorSubdivisionType(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        super().clean()
        validate_unique_case_insensitive(self.name, SectorSubdivisionType, 'name', self)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subcity(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        super().clean()
        validate_unique_case_insensitive(self.name, Subcity, 'name', self)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubcitySubdivisionType(models.Model):
    class SubcityType(models.TextChoices):
        WOREDA = 'Woreda', 'Woreda'

    name = models.CharField(
        max_length=20,
        choices=SubcityType.choices,
        default=SubcityType.WOREDA
    )

    def __str__(self):
        return self.name

class Woreda(models.Model):
    name = models.CharField(max_length=50)
    subcity = models.ForeignKey(Subcity, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['name', 'subcity']

    def clean(self):
        super().clean()
        # Check for case-insensitive uniqueness within the same subcity
        lookup = {
            'name__iexact': self.name,
            'subcity': self.subcity
        }
        if self.pk:
            lookup['pk__ne'] = self.pk
        
        if Woreda.objects.filter(**lookup).exists():
            raise DuplicateEntryError(
                'woreda',
                'name',
                f"{self.name} in {self.subcity.name}"
            )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.subcity}"

class OrganizationalUnit(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    required_employees_no = models.IntegerField()
    sector_subdiv_type = models.ForeignKey(
        SectorSubdivisionType, on_delete=models.PROTECT, null=True, blank=True
    )
    subcity_subdiv_type = models.ForeignKey(
        SubcitySubdivisionType, on_delete=models.PROTECT, null=True, blank=True
    )
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True
    )
    subcity = models.ForeignKey(Subcity, on_delete=models.PROTECT, null=True, blank=True)
    woreda = models.ForeignKey(Woreda, on_delete=models.PROTECT, null=True, blank=True)

    def clean(self):
        super().clean()
        if self.sector_subdiv_type is not None and self.subcity_subdiv_type is not None:
            raise DjangoValidationError(
                "Sector Subdivision Type and Subcity Subdivision Type are mutually exclusive. You cannot select both."
            )
        validate_unique_case_insensitive(self.name, OrganizationalUnit, 'name', self)
    
    def save(self, *args, **kwargs):
        # If this unit has a parent, inherit the fields if they're not set
        if self.parent:
            if not self.division:
                self.division = self.parent.division
            if not self.sector_subdiv_type:
                self.sector_subdiv_type = self.parent.sector_subdiv_type
            if not self.subcity_subdiv_type:
                self.subcity_subdiv_type = self.parent.subcity_subdiv_type
            if not self.subcity:
                self.subcity = self.parent.subcity
            if not self.woreda:
                self.woreda = self.parent.woreda
        
        self.name = self.name.upper()
        self.full_clean()
        super().save(*args, **kwargs)
                
    def __str__(self):
        return self.name
    
class EmployeeRole(models.Model): 
    class RoleType(models.TextChoices):
        DIRECTOR = 'Director', 'Director'
        # LEADER = 'Subcity', 'Subcity' 
        EXPERT = 'Expert', 'Expert'
        # HOSPITAL = 'Hospital', 'Hospital'

    role = models.CharField(
        max_length=50,
        choices=RoleType.choices
    )

    def __str__(self):
        return self.role

class Employee(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50, unique=True)
    organizationalunit = models.ForeignKey(OrganizationalUnit, on_delete=models.PROTECT)
    role = models.ForeignKey(EmployeeRole, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return f"{self.fname} {self.mname}"
