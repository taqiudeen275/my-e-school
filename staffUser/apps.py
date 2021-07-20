from django.apps import AppConfig


class StaffuserConfig(AppConfig):
    name = 'staffUser'

    def ready(self):
        import staffUser.signals
