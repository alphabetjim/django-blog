# Generated by Django 4.2.10 on 2024-03-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_appointment_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(choices=[('Monday 2024-03-04', '2024-03-04'), ('Tuesday 2024-03-05', '2024-03-05'), ('Wednesday 2024-03-06', '2024-03-06'), ('Thursday 2024-03-07', '2024-03-07'), ('Friday 2024-03-08', '2024-03-08'), ('Monday 2024-03-11', '2024-03-11'), ('Tuesday 2024-03-12', '2024-03-12'), ('Wednesday 2024-03-13', '2024-03-13'), ('Thursday 2024-03-14', '2024-03-14'), ('Friday 2024-03-15', '2024-03-15')], max_length=20),
        ),
    ]
