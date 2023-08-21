from django.db import models
from accounts.models import User
# import rules



class Alert(models.Model):
    title = models.CharField(max_length=200, default = "Alert")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product_name = models.CharField(max_length=200)
    expiry_date = models.DateTimeField()
    batch_no = models.CharField(default = "true")

    class Meta:
        ordering = ["expiry_date"]

    def __str__(self):
        return f"{self.title} at {self.time}"
    def get_absolute_url(self):
        return "/"
    
    