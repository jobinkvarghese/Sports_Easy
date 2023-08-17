# Generated by Django 4.1.2 on 2023-08-16 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0077_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 16, 11, 37, 25, 111043)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 16, 11, 37, 25, 110043)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 23, 11, 37, 25, 108041)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 16, 11, 37, 25, 108041)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 16, 11, 37, 25, 113040)
            ),
        ),
    ]