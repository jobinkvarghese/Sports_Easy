# Generated by Django 4.1.6 on 2023-04-03 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_complaint_reg_tbl_status_alter_booking_arrival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 15, 23, 12, 861981)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 15, 23, 12, 861981)),
        ),
        migrations.AlterField(
            model_name='complaint_reg_tbl',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 15, 23, 12, 861981)),
        ),
    ]
