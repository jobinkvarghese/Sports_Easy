# Generated by Django 4.1.6 on 2023-05-09 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0043_alter_academy_admission_tbl_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy_admission_tbl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 18, 22, 92092)),
        ),
        migrations.AlterField(
            model_name='academy_admission_tbl',
            name='eml',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='book_event_tbl',
            name='bookingdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 18, 22, 92092)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 12, 18, 22, 92092)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 18, 22, 92092)),
        ),
        migrations.AlterField(
            model_name='turf_booking_tbl',
            name='tdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 18, 22, 92092)),
        ),
    ]