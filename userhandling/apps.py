from django.apps import AppConfig


class UserhandlingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userhandling'

    def ready(self):
        import userhandling.signals