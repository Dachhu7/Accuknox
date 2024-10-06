from django.apps import AppConfig

class SignalsAppConfig(AppConfig):
    name = 'signals_app'

    def ready(self):
        # Import and register the signal handlers
        import signals_app.signals
