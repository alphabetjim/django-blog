from django.db import models
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

# day choices
def weekdays_next_fortnight():
    today = date.today()
    weekdays_ahead = []
    for i in range(14):
        day_ahead = today + timedelta(i+1)
        if day_ahead.strftime('%w')!='0' and day_ahead.strftime('%w')!='6':
            weekdays_ahead.append((str(day_ahead), f"{day_ahead.strftime('%A')} {str(day_ahead)}"))
    return tuple(weekdays_ahead)
DAY_CHOICES = weekdays_next_fortnight()
    


class Appointment(models.Model):
    """
    Stores a single appointment, related to User.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="appts")
    day = time = models.CharField(max_length=10, choices=DAY_CHOICES)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"  