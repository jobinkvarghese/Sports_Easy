# Generated by Django 4.1.2 on 2023-07-19 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0052_newcartadd_qty_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newcartadd",
            name="netprice",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=99),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 13, 1, 4, 581870)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 13, 1, 4, 581870)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 26, 13, 1, 4, 580870)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 13, 1, 4, 580870)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 13, 1, 4, 582870)
            ),
        ),
    ]