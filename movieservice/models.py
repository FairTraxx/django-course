from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, null=False)
    overview = models.CharField(max_length= 1000, null= True)
    average_vote = models.CharField(max_length=20, null= False)
    user_rating = models.IntegerField(null= True)
    user_id = models.ForeignKey(User, max_length= 30, on_delete = models.CASCADE)
 