from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Category(models.Model):
    """Model definition for Category."""

    categorie = models.CharField(max_length = 150)
    description = models.TextField(null=True, blank=True)
    
    

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Category."""
        return self.categorie


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150, blank=True, null=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    category = models.ManyToManyField(Category, verbose_name=("Categoria"))
    
    
    

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title