# Generated by Django 4.1.6 on 2023-04-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eimage', models.FileField(upload_to='pictures')),
                ('eaddress', models.CharField(max_length=100)),
                ('eloc', models.URLField()),
                ('edate', models.DateField()),
                ('ticket', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('details', models.CharField(max_length=150)),
                ('pass1', models.CharField(max_length=15)),
                ('cpass', models.CharField(max_length=15)),
                ('dist', models.CharField(max_length=25)),
                ('Approve', models.BooleanField(default=True)),
            ],
        ),
    ]
