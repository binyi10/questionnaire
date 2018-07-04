from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class users(models.Model):
    ip = models.TextField(null = False)
    now_query_id = models.IntegerField()
class dataQuery2(models.Model):
    item = models.TextField(null = True)
    item_google = models.TextField(null = True)
    item_bing = models.TextField(null = True)
class results_final(models.Model):
    ip = models.TextField(null = False)
    query_id = models.IntegerField()
    answer = models.TextField(null = False)
    comment = models.TextField(null = True)