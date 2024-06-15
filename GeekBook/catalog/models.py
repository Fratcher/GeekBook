from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field


# Create your models here.
class Image(models.Model):
    '''Model representing an Image'''
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='images/'
    )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular image instance."""
        return reverse('image-detail', args=[str(self.id)])


class Year(models.Model):
    """Model representing a year."""
    name = models.IntegerField(
        unique=True,
        help_text="Enter valid year format (e.g. 1999, 2021, etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('year-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='year_name_case_insensitive_unique',
                violation_error_message = "Year already exists (case insensitive match)"
            ),
        ]

class Description(models.Model):
    """Model representing a Description."""
    desc = models.CharField(max_length=400)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books.
    # Author as a string rather than object because it hasn't been declared yet in file.

    summary = models.TextField(
        max_length=1000, help_text="What is the story behind this one?? :)")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    year = models.ManyToManyField(
        Year, help_text="Select a Year for this entry")

    def __str__(self):
        """String for representing the Model object."""
        return self.desc

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('desc-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
