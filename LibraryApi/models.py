from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    is_booked = models.BooleanField(default=False)
    category = models.CharField(max_length=255)  # Add a category field

    def __str__(self):
        return self.title


class User(models.Model):
  username = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  password = models.CharField(max_length=255)
  def __str__(self):
      return self.username



class Booking(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  booking_date = models.DateField()

  def __str__(self):
    return f'Booking for {self.book.title}'

