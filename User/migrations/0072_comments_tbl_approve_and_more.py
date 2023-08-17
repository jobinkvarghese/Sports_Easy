# Generated by Django 4.1.2 on 2023-08-09 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0071_posts_tbl_approve_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments_tbl",
            name="approve",
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 9, 18, 5, 25, 507447)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 9, 18, 5, 25, 506446)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 16, 18, 5, 25, 506446)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 9, 18, 5, 25, 506446)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 9, 18, 5, 25, 508446)
            ),
        ),
    ]
