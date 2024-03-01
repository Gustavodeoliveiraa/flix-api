from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movies


class Review(models.Model):
    movie = models.ForeignKey(
        Movies, on_delete=models.PROTECT,
        related_name='review'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação nao pode ser inferior a 0'),
            MaxValueValidator(5, 'Avaliação nao pode ser superior a 5')
        ]
    )
    comment = models.TextField()

    def __str__(self):
        return str(self.movie)
