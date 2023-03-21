"""
Configuration for ekozumi_app
"""
from django.apps import AppConfig

class EkozumiAppConfig(AppConfig):
    """
    General configuration for the ekozumi application

    Args:
        AppConfig : Default configuration for Apps
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "ekozumi_app"
