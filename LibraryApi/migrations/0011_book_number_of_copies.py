# Generated by Django 4.2.7 on 2024-04-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApi', '0010_alter_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number_of_copies',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]