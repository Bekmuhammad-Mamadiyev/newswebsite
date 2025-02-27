from django.db import models
from django.urls import reverse
from django.utils import timezone


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NewsModel(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='media/images/')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=Status.choices, max_length=2, default=Status.Draft)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_page', args=[self.slug])


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email
