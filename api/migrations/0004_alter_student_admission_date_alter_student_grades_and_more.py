# Generated by Django 5.0.7 on 2024-07-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='grades',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
