from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Division, SubcitySubdivisionType

@receiver(post_migrate)
def default_data(sender, **kwargs):
    default_divisions = [
        "Sector Office",
        "Subcity",
        "College",
        "Hospital"
    ]
    default_subcity_subdiv = "Woreda"
    
    for name in default_divisions:
        Division.objects.get_or_create(name=name)
    
    SubcitySubdivisionType.objects.get_or_create(name=default_subcity_subdiv)    
    

