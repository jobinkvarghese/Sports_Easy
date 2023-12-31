# Generated by Django 4.1.6 on 2023-04-24 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0032_alter_academy_admission_tbl_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy_admission_tbl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 29, 36, 967820)),
        ),
        migrations.AlterField(
            model_name='book_event_tbl',
            name='bookingdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 29, 36, 967820)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 1, 21, 29, 36, 967820)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 29, 36, 967820)),
        ),
        migrations.AlterField(
            model_name='comments_tbl',
            name='comment',
            field=models.TextField(default='nocomments'),
        ),
    ]
