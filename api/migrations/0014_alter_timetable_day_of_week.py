# Generated by Django 5.0.7 on 2024-07-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_event_unique_together_event_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day_of_week',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10),
        ),
    ]
