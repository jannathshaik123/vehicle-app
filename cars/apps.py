from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    
    def ready(self):
        ## set up the signals
        import cars.signals
        # This will import the signals module when the app is ready
        # and ensure that any signal handlers are connected.
