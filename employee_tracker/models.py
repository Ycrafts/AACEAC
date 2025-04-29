from django.db import models

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
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subcity(models.Model):
    name = models.CharField(max_length=50)

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
    subcity = models.ForeignKey(Subcity, on_delete=models.PROTECT)      # cant delete subcity if linked to woreda

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
    phone_no = models.CharField(max_length=50)
    organizationalunit = models.ForeignKey(OrganizationalUnit, on_delete=models.PROTECT)
    role = models.ForeignKey(EmployeeRole, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.mname}"
