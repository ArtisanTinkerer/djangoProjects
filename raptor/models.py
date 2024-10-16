from django.conf import settings
from django.db import models
from django.utils import timezone

class Sighting(models.Model):
    class Status(models.TextChoices):
        # names, values, labels
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    spotter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'made_sightings'
    )

    body = models.TextField()
    when = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-when']
        indexes = [
            models.Index(fields=['-when']),
        ]

    def __str__(self):
        return self.title