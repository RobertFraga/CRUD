from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10, blank=True, null=True)
    second_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user'

