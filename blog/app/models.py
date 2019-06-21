from django.db import models
from tinymce import HTMLField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250, null=True)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:detail", kwargs={"pk": self.id})