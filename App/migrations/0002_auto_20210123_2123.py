# Generated by Django 3.1.3 on 2021-01-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='student_id',
            field=models.CharField(max_length=255),
        ),
    ]
