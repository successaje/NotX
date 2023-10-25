from django.db import models

# import rules



class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default = "Alert")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product_name = models.CharField(max_length=200)
    expiry_date = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    batch_no = models.CharField(max_length=200, default = "true")
    expired = models.BooleanField(default=False, blank=False)

    objects = models.Manager()
    class Meta:
        ordering = ["expiry_date"]

    def __str__(self):
        return f"{self.title} at {self.time}"
    def get_absolute_url(self):
        return "/"
    
    