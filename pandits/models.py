from django.db import models

class Pandit(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(default = 0)
    specialization = models.CharField(max_length=100, default= "General Puja")
    availability = models.BooleanField(default=True)
    contact_info = models.CharField(max_length = 12, default = 00)
    languages = models.CharField(max_length=100 , default = "Marathi")
    location = models.CharField(max_length=100,default = "Swarg")
    email = models.EmailField( unique=True, default = "abc@xyz.com")

    def __str__(self):
        return self.name

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 500)


    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pandits = models.ManyToManyField(Pandit)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pandit = models.ForeignKey(Pandit, on_delete= models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 500)

    def __str__(self):
        return f"{self.user.name} - {self.pandit.name} - {self.service.name} on {self.date}"
    

    


