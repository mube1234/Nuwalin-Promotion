from django.apps import AppConfig


class PromotionConfig(AppConfig):
    name = 'promotion'
    def ready(self):
        import promotion.signals
