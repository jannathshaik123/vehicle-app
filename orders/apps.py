from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    
    def ready(self):
        """
        This method is called when the app is ready.
        It can be used to import signals or perform any initialization tasks.
        """
        # Import the signals module to ensure signals are registered
        import orders.signals
