from django.db import models
from django.core.validators import RegexValidator

# model Mailing
class MailingList(models.Model):
    date_start = models.DateTimeField(verbose_name='Mailing start date')
    time_start = models.TimeField(verbose_name='Mailing start time')
    date_end = models.DateTimeField(verbose_name='Mailing end date')
    time_end = models.TimeField(verbose_name='Mailing end time')
    message = models.TextField( verbose_name='Message text', max_length=255)
    tag = models.CharField(verbose_name='Search by tags', max_length=100, blank=True)
    mobile_operator_code = models.CharField(verbose_name='Search by code', max_length=3, blank=True)

    def __str__(self):
        return f'Mailing list {self.id} from {self.date_start}'

    class Meta:
        verbose_name = 'Mailing List'
        verbose_name_plural = 'Mailing Lists'


# model Client
class Client(models.Model):

    phone_number_regex = RegexValidator(regex=r'^7\w{10}$',
                                        message="Enter the client's phone number at the following format: 7XXXXXXXXXX")
    phone_number = models.CharField(verbose_name='Phone number', validators=[phone_number_regex], unique=True, max_length=11)
    mobile_operator_code = models.CharField(verbose_name='Mobile operator code', max_length=3, editable=False)
    tag = models.CharField(verbose_name='Search by tags', max_length=100, blank=True)
    timezone = models.CharField(verbose_name='Time zone',max_length=32, default='UTC')

    # def save(self, *args, **kwargs):
    #     self.mobile_operator_code = str(self.phone_number)[1:4]
    #     return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'Client {self.id} with number {self.phone_number}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


# model Message
class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    date_time_sending = models.DateTimeField(verbose_name='Time create', auto_now_add=True)
    status = models.CharField(verbose_name='status', max_length=15, choices=STATUS_CHOICES)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Id of client')

    def __str__(self):
        return f'Message {self.id} with text {self.mailing_list} for {self.client}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-id']