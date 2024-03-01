from django.db import models

class ReversedIPRecord(models.Model):
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reversed IP: {self.ip}"