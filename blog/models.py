from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

# class Podcast(models.Model):
#     audio = models.FileField(upload_to="records")
#     language = models.CharField(max_length=50, null=True, blank=True)

#     class Meta:
#         verbose_name = "Record"
#         verbose_name_plural = "Records"

#     def __str__(self):
#         return str(self.id)

#     def get_absolute_url(self):
#         return reverse("record_detail", kwargs={"id": str(self.id)})


class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    image=models.ImageField( upload_to="images/",null=True)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
