# Generated by Django 4.2.10 on 2024-03-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_appointment_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(choices=[('2024-03-04', 'Monday 2024-03-04'), ('2024-03-05', 'Tuesday 2024-03-05'), ('2024-03-06', 'Wednesday 2024-03-06'), ('2024-03-07', 'Thursday 2024-03-07'), ('2024-03-08', 'Friday 2024-03-08'), ('2024-03-11', 'Monday 2024-03-11'), ('2024-03-12', 'Tuesday 2024-03-12'), ('2024-03-13', 'Wednesday 2024-03-13'), ('2024-03-14', 'Thursday 2024-03-14'), ('2024-03-15', 'Friday 2024-03-15')], max_length=10),
        ),
    ]