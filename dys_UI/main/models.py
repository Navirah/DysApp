#django

from django.db import models

class File(models.Model):
    picture=models.ImageField(upload_to='pictures')
    class Meta:
        db_table='files'
