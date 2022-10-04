from django.db import models



# Create your models here.
class Directory(models.Model):
    first_name= models.TextField(max_length=20)
    last_name= models.TextField(max_length=20)
    other_name=models.TextField(max_length=20, null=True)
    tel=models.TextField(unique=True, max_length=11)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    

    
    