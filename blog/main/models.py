from django.db import models


class Post(models.Model):
    name = models.CharField('Author', max_length=255)
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Full text')
    likes = models.PositiveIntegerField('Likes')

    def __str__(self):
        return self.name
