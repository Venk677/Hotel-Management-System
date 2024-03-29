# Generated by Django 2.2.6 on 2019-10-19 10:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_id', models.IntegerField()),
                ('hotel_location', models.CharField(max_length=100)),
                ('hotel_contact', models.IntegerField()),
                ('no_of_rooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('max_guests', models.IntegerField()),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_manager_name', models.CharField(max_length=100)),
                ('manager_contact_no', models.IntegerField()),
                ('hotel_manager_id', models.IntegerField()),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_address', models.CharField(max_length=100)),
                ('guest_contact', models.IntegerField()),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_in', models.DateField(default=datetime.date(2019, 10, 19))),
                ('log_out', models.DateField(default=datetime.date(2019, 10, 20))),
                ('check_out', models.BooleanField(default=False)),
                ('guest_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelapp.Guest')),
                ('hotel_manager_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelapp.Manager')),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelapp.Hotel')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelapp.Room')),
            ],
        ),
    ]
