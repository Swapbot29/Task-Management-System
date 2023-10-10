from django.db import models

# Create your models here.

class Task(models.Model):
    to_do = "TD"
    in_progress = "IP"
    done = "DN"
    status_choices = [
        (to_do, "To Do"),
        (in_progress, "In Progress"),
        (done, "Done"),
    ]
    team_member = models.CharField(max_length=100,null=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200,null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=2,choices=status_choices,default="TD")

    def __str__(self):
        return self.title