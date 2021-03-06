from django.db import models
from django.core.validators import MinValueValidator


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
    )
    description = models.CharField(
        max_length=100,
        default='',
    )
    author = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f'{self.author}   "{self.title}"'

