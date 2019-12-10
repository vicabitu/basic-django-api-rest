from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{} - {} - {} - Books: {}".format(self.name, self.last_name, self.nationality, self.books.all().values_list('title'))

class Book(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    edition = models.PositiveIntegerField(blank=True, null=True)
    editorial = models.CharField(max_length=60, blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    available_quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "{} - Edition: {}".format(self.title, self.edition)
