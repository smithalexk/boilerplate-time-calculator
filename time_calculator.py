import re


def add_time(start, duration, day=None):
    hours = [int(re.search("([0-9]+):", x).groups()[0]) for x in [start, duration]]
    minutes = [int(re.search(":([0-9]+)", x).groups()[0]) for x in [start, duration]]

    if "PM" in start:
        hours[0] = hours[0] + 12

    total_hours = sum(hours)
    total_minutes = sum(minutes)

    total_hours += total_minutes // 60

    days = total_hours // 24
    
    am_pm_flag = "AM" if total_hours % 24 < 12 else "PM"

    o_hours = total_hours % 24
    if o_hours > 12:
        o_hours -= 12
    
    o_minutes = total_minutes % 60

    new_time = f"{o_hours}:{o_minutes:02d} {am_pm_flag}"

    if days == 1:
        new_time = " ".join([new_time, "(next day)"])
    elif days > 1:
        new_time = " ".join([new_time,f"({days} days later)"])

    return new_time