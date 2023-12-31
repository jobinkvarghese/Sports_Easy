# Generated by Django 4.1.2 on 2023-07-19 10:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0053_newcartadd_netprice_alter_academy_admission_tbl_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 37, 5, 973974)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 37, 5, 972974)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 26, 15, 37, 5, 971974)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 37, 5, 971974)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 37, 5, 974973)
            ),
        ),
        migrations.CreateModel(
            name="Fullpayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdate", models.DateField(auto_now=True)),
                ("paydate", models.DateField()),
                ("netprice", models.DecimalField(decimal_places=2, max_digits=99)),
                ("status", models.CharField(max_length=100)),
                (
                    "newcartid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="User.newcartadd",
                    ),
                ),
            ],
        ),
    ]
