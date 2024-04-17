from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
      #user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
      title = models.CharField(max_length=100)
      author = models.CharField(max_length=100)
      body = models.TextField()
      date_added = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.author