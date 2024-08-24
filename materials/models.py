
from django.db import models


# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True)
    slug = models.CharField(max_length=150,verbose_name='slug', null=True, blank=True)


    def _str__(self):
        return f"{self.title} {self.body} {self.is_published}"



    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
