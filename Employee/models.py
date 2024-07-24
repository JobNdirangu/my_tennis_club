from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=10)

    #this tell djdango the name of the table if you dont want to go with the default 
    class Meta:
        db_table="employee"

    # def __str__(self):
    #     return self.name


