# Generated by Django 5.0.4 on 2024-05-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0009_hobbie_hotel_owners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbie',
            name='hotel_owners',
        ),
        migrations.RemoveField(
            model_name='hobbie',
            name='persons',
        ),
        migrations.AddField(
            model_name='person',
            name='hobbies',
            field=models.ManyToManyField(to='booking_app.hobbie'),
        ),
    ]