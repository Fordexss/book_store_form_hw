from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    published_date = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.title
