# newsfeed/apps.py

from django.apps import AppConfig

class NewsfeedConfig(AppConfig):
    name = 'newsfeed'

    def ready(self):
        import newsfeed.signals
