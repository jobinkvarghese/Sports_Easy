# Generated by Django 4.1.2 on 2023-08-14 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0074_book_event_tbl_cancel_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Out For Shipping", "Out For Shipping"),
                    ("Completed", "Completed"),
                    ("Cancel", "Cancel"),
                ],
                default="Pending",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 11, 1, 53, 599278)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 11, 1, 53, 599278)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 21, 11, 1, 53, 598310)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 11, 1, 53, 598310)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 11, 1, 53, 600312)
            ),
        ),
    ]
