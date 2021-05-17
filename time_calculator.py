import re


weekdays = {
    1: "sunday",
    2: "monday",
    3: "tuesday",
    4: "wednesday",
    5: "thursday",
    6: "friday",
    7: "saturday",
}


def add_time(start: str, duration: str, day: str = None) -> str:
    hours = [int(re.search("([0-9]+):", x).groups()[0]) for x in [start, duration]]
    minutes = [int(re.search(":([0-9]+)", x).groups()[0]) for x in [start, duration]]
    
    if "PM" in start:
        hours[0] = hours[0] + 12

    total_hours = sum(hours)
    total_minutes = sum(minutes)

    total_hours += total_minutes // 60

    days = total_hours // 24

    if day:
        day_num = next((num for num, wd in weekdays.items() if wd == day.lower()), None)
        
        day_num += days


    am_pm_flag = "AM" if total_hours % 24 < 12 else "PM"

    o_hours = total_hours % 24
    if o_hours > 12:
        o_hours -= 12
    elif o_hours == 0:
        o_hours = 12

    o_minutes = total_minutes % 60

    new_time = f"{o_hours}:{o_minutes:02d} {am_pm_flag}"

    if day:
        new_time = ", ".join([new_time, weekdays[day_num % 7].capitalize()])

    if days == 1:
        new_time = " ".join([new_time, "(next day)"])
    elif days > 1:
        new_time = " ".join([new_time, f"({days} days later)"])


    return new_time