# Generated by Django 4.1.2 on 2023-07-12 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0046_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 16, 53, 19, 676450)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 16, 53, 19, 675451)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 16, 53, 19, 674451)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 16, 53, 19, 674451)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 16, 53, 19, 677450)
            ),
        ),
    ]
