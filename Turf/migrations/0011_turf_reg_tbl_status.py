# Generated by Django 4.1.2 on 2023-08-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Turf", "0010_turf_reg_tbl_approve"),
    ]

    operations = [
        migrations.AddField(
            model_name="turf_reg_tbl",
            name="status",
            field=models.CharField(default="nill", max_length=100),
        ),
    ]
