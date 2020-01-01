from django.db import models
import datetime as dt
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=32)
    location = models.CharField(max_length=70)
    date = models.DateField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to= 'thumbnails/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    useremail = models.EmailField()
    usermessage = models.TextField()

    def __str__(self):
        return self.fullname

class EventImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    event = models.ForeignKey('event', related_name = 'eventimages', on_delete=models.PROTECT)
