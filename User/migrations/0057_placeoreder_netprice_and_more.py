# Generated by Django 4.1.2 on 2023-07-23 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0056_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="placeoreder",
            name="netprice",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 15, 39, 57, 138555)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 15, 39, 57, 137586)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 30, 15, 39, 57, 136585)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 15, 39, 57, 136585)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 15, 39, 57, 139585)
            ),
        ),
    ]