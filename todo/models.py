from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class CreateTodo(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, null=False ,default="")
    desc = models.TextField(null=False, default="")
    crateDt = models.DateField(auto_now_add = True)
    expectedDateTime = models.DateTimeField(default = now)


    def __str__(self):
        return f"{self.title}: {self.desc[0:10]}"