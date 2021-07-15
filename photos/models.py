from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(blank=True, null=True, upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} {self.id}'

# Create your models here.
