from django.db import models



class Position(models.Model):
    title_choice=(
    ('Manager','Manager'),
    ('IT Technician','IT Technician'),
    ('Sales Person', 'Sales Person')
    )
    title=models.CharField(max_length=50,choices=title_choice)

    def __str__(self):
        return self.title
class Education(models.Model):
    education_choice=(
    ('PHD','PHD'),
    ('Masters','Masters'),
    ('Under Graduate','Under Graduate'),
    ('Form Four Leaver','Form Four Leaver')
    )

    level_of_education=models.CharField(max_length=40,choices=education_choice)

    def __str__(self):
        return self.level_of_education

class Employee(models.Model):
    full_name=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=30,unique=True)
    mobile=models.CharField(max_length=14,unique=True)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    education=models.ForeignKey(Education,on_delete=models.CASCADE)
    cv=models.FileField(upload_to=f'CV',blank=True,null=True)
    about=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to=f'DP',blank=True,null=True)

    def __str__(self):
        return f'{self.full_name} ({self.position.title})'
