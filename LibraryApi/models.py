from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    is_booked = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Reference to the User model
    publisher = models.CharField(max_length=255 ,  default=None , null=True)  # Name of the publisher
    published_place = models.CharField(max_length=255 ,  default=None , null=True)  # Place where the book is published
    page_number = models.IntegerField( default=None , null=True)  # Number of pages in the book
    dewey_decimal_number = models.CharField(max_length=255 , default=None , null=True)  # Dewey Decimal number (e.g., 999-k)
    dewey_decimal_category_range = models.CharField(max_length=255 , default=None , null=True)  # Dewey Decimal category range
    book_code = models.IntegerField(default=None , null=True) 
    updated_by = models.IntegerField(default=None , null=True) 


    def __str__(self):
        return self.title



class Booking(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  booking_date = models.DateField()

  def __str__(self):
    return f'Booking for {self.book.title}'

