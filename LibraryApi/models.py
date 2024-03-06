from django.db import models

# Create your models here.

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


    def __str__(self):
        return self.title


class User(models.Model):
  username = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  password = models.CharField(max_length=255)
  def __str__(self):
      return self.username


# desc of order books

class Booking(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  booking_date = models.DateField()

  def __str__(self):
    return f'Booking for {self.book.title}'

