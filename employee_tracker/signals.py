from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Division, SubcitySubdivisionType, SectorSubdivisionType, EmployeeRole, Subcity, Woreda

@receiver(post_migrate)
def default_data(sender, **kwargs):
    # Default divisions
    default_divisions = [
        "Sector Office",
        "Subcity",
        "College",
        "Hospital"
    ]
    
    # Default sector subdivision types
    default_sector_subdivs = [
        "Commission",
        "Corporation",
        "Bureau",
        "Agency"
    ]
    
    # Default subcity subdivision type
    default_subcity_subdiv = "Woreda"
    
    # Default employee roles
    default_employee_roles = [
        "Director",
        "Expert"
    ]
    
    # Sample subcities and their woredas
    subcity_woreda_data = {
        "Addis Ketema": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Akaki Kaliti": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Arada": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Bole": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Gullele": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Kirkos": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Kolfe Keranio": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Lideta": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Nifas Silk-Lafto": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "Yeka": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
    }
    
    # Create divisions
    for name in default_divisions:
        Division.objects.get_or_create(name=name)
    
    # Create sector subdivision types
    for name in default_sector_subdivs:
        SectorSubdivisionType.objects.get_or_create(name=name)
    
    # Create subcity subdivision type
    SubcitySubdivisionType.objects.get_or_create(name=default_subcity_subdiv)
    
    # Create employee roles
    for role in default_employee_roles:
        EmployeeRole.objects.get_or_create(role=role)
    
    # Create subcities and their woredas
    for subcity_name, woreda_numbers in subcity_woreda_data.items():
        subcity, _ = Subcity.objects.get_or_create(name=subcity_name)
        for woreda_number in woreda_numbers:
            Woreda.objects.get_or_create(
                name=f"Woreda {woreda_number}",
                subcity=subcity
            )    

