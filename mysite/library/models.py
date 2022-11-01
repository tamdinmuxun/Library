from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date')

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return f"{str(self.author)}. {self.title}"
