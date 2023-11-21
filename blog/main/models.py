from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    name = models.CharField('Author', max_length=255)
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Full text')
    tag_list = models.ManyToManyField('Tags', blank=True)
    likes = models.PositiveIntegerField('Likes')
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True, null=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Post, self).save(force_insert, force_update, using, update_fields)


class Tags(models.Model):
    name = models.CharField('Tag name', max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
