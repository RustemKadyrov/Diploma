from django.apps import AppConfig


class CabinetConfig(AppConfig):
    name = 'cabinet'

    def ready(self) -> None:
        import cabinet.signals  # noqa
