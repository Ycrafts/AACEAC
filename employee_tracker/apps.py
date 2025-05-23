from django.apps import AppConfig


class EmployeeTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee_tracker'
    
    def ready(self):
        import employee_tracker.signals
