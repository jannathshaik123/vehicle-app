from django.apps import AppConfig


class BuyersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buyers'
    
    def ready(self):
        ## set up the signals
        import buyers.signals
