from django.apps import AppConfig


class CalcConfig(AppConfig):
    name = 'calc'

    def ready(self):
        import calc.signals
