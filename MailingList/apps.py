from django.apps import AppConfig

class MailingListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MailingList'

    def ready(self):
        from MailingList import signals