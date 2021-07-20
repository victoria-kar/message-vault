from django.db import models

# Create your models here.
class Messages(models.Model):
    username = models.CharField(max_length=120, default="Anonymous")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.message}"
