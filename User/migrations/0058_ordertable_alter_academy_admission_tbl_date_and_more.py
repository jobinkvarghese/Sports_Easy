# Generated by Django 4.1.2 on 2023-07-23 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0057_placeoreder_netprice_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderTable",
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
                ("order_number", models.CharField(max_length=10)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "order_table",},
        ),
        migrations.AlterField(
            model_name="academy_admission_tbl",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 16, 7, 5, 397140)
            ),
        ),
        migrations.AlterField(
            model_name="book_event_tbl",
            name="bookingdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 16, 7, 5, 396140)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="arrival_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 30, 16, 7, 5, 396140)
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 16, 7, 5, 396140)
            ),
        ),
        migrations.AlterField(
            model_name="turf_booking_tbl",
            name="tdate",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 23, 16, 7, 5, 398140)
            ),
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "ordertable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="User.ordertable",
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={"db_table": "order_item",},
            bases=("User.ordertable",),
        ),
    ]
