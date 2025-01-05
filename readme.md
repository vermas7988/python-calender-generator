# Schedule Generator

This Python script generates an iCalendar (.ics) file for a predefined schedule for weekdays in January 2025. The generated calendar includes events such as waking up, working out, meals, work, and other activities.

## Prerequisites

- Python 3.x
- `icalendar` library

## Installation

1. Clone the repository or download the script.
2. Install the required `icalendar` library using pip:

    ```sh
    pip install icalendar
    ```

## Usage

1. Run the script:

    ```sh
    python cal.py
    ```

2. The script will generate an iCalendar file named [january_2025_schedule.ics](http://_vscodecontentref_/0) in the same directory.

## Customization

### Changing the Schedule

To modify the schedule, update the [schedule](http://_vscodecontentref_/1) list in the script. Each entry in the list is a tuple containing the activity name, start time, and duration in minutes. For example:

```python
schedule = [
    ("Wake up and coffee", "6:00 AM", 30),
    ("Work out and stretching", "6:30 AM", 60),
    # Add or modify activities here
]
```

### Changing the Base Date

The base date for the schedule is set to January 1, 2025. To change the base date, modify the base_date variable:

```python
    base_date = datetime(2025, 1, 1)  # Change the year, month, and day as needed
```

### Including Weekends
By default, the script skips weekends (Saturdays and Sundays). To include weekends, remove or modify the following lines:


### Changing the Output File Name
The output file name is set to january_2025_schedule.ics. To change the file name, modify the following line:

## Notes
The generated iCalendar file can be imported into calendar applications like Google Calendar, apple Calender, Outlook, etc.