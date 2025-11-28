from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100) #varchar(100)
    content = models.TextField()#text
    create_at = models.DateTimeField(auto_now_add=True)  #timestamp

    def __str__(self):
        return self.title