# Generated by Django 4.2.7 on 2024-03-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApi', '0009_booking_admin_booking_deadline_date_booking_isbooked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default='2024-01-09', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='deadline_date',
            field=models.DateField(default='2024-01-09', null=True),
        ),
    ]
