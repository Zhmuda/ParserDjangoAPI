from django.db import models

class Cinema(models.Model):
    data_order = models.IntegerField()
    full_name = models.TextField()
    objects_of_examination = models.TextField()
    city = models.CharField(max_length=255)
    fo = models.CharField(max_length=255)
    e_mail = models.EmailField()
    order_date = models.DateTimeField()
    order_number = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
