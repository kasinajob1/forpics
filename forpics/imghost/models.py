from django.db import models
from thumbs import ImageWithThumbsField

# Create your models here.
class Picture(models.Model):
      image = ImageWithThumbsField(upload_to='images', sizes=((200,150),))
