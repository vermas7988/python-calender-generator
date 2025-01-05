from icalendar import Calendar, Event
from datetime import datetime, timedelta

# you will need to install the icalendar library if you haven't already
# pip install icalendar
# Create a calendar object
cal = Calendar()

# Define the schedule
schedule = [
    ("Wake up and coffee", "6:00 AM", 30),
    ("Work out and stretching", "6:30 AM", 60),
    ("Breakfast", "7:30 AM", 30),
    ("Getting ready, lunch prep, and travel to office if needed", "8:00 AM", 40),
    ("Work", "8:40 AM", 200),  # Till 12:00 PM
    ("Lunch", "12:00 PM", 60),
    ("Work", "1:00 PM", 180),  # Till 4:00 PM
    ("Work, Talk with parents etc.", "4:00 PM", 60),
    ("Snacks and fruits", "5:00 PM", 30),
    ("Go out for a walk", "5:30 PM", 60),
    ("Dinner prep, eating and cleaning", "6:30 PM", 90),
    ("Work", "8:00 PM", 150),  # Till 10:30 PM
    ("Sleep", "10:30 PM", 450),  # Till 6:00 AM
]

# Base date (January 1, 2025)
base_date = datetime(2025, 1, 1)

# Add events for each weekday in January 2025
for day_offset in range(31):  # January has 31 days
    day_date = base_date + timedelta(days=day_offset)
    if day_date.weekday() >= 5:  # Skip Saturdays (5) and Sundays (6)
        continue
    for activity, start_time, duration_minutes in schedule:
        # Calculate start and end times
        start_hour, start_minute = map(int, start_time[:-3].split(":"))
        start_hour += 12 if "PM" in start_time and start_hour != 12 else 0
        start_hour -= 12 if "AM" in start_time and start_hour == 12 else 0
        start_datetime = day_date.replace(hour=start_hour, minute=start_minute)
        end_datetime = start_datetime + timedelta(minutes=duration_minutes)

        # Create an event
        event = Event()
        event.add("summary", activity)
        event.add("dtstart", start_datetime)
        event.add("dtend", end_datetime)
        event.add("dtstamp", datetime.now())
        cal.add_component(event)

# Save the calendar to a file
with open("january_2025_schedule.ics", "wb") as f:
    f.write(cal.to_ical())

print("iCal file created: january_2025_schedule.ics")
