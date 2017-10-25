from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    mobile_no = models.IntegerField()
    message = models.TextField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Contact {}'.format(self.id)
