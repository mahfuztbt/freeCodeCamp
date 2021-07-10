def add_time(start, duration, start_day=0):

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if start_day != 0:
        start_day = start_day.lower()
        start_day = start_day.capitalize()
    else:
        start_day = "Not provided"

    time_start = start.split(" ")
    if time_start[1] == "PM":
        time_start = time_start[0].split(":")
        time_start = (int(time_start[0]) + 12) * 60 + int(time_start[1])
    else:
        time_start = time_start[0].split(":")
        time_start = int(time_start[0]) * 60 + int(time_start[1])

    time_duration = duration.split(":")
    time_duration = int(time_duration[0]) * 60 + int(time_duration[1])

    time_end = time_start + time_duration

    day = time_end // 1440
    hour = (time_end - day * 1440) // 60
    minute = time_end - (hour * 60) - (day * 1440)
    meridiem = "AM" if hour < 12 else "PM"
    hour = hour - 12 if hour > 12 else hour
    hour = 12 if hour == 0 else hour
    minute = "0" + str(minute) if minute < 10 else str(minute)

    if day == 0:
        days_passed = ""
    elif day == 1:
        days_passed = "(next day)"
    else:
        days_passed = f"({day} days later)"

    if start_day == "Not provided":
        end_day = ""
    else:
        week_count = day % 7
        week_start = week_days.index(start_day)

        if week_count + week_start > 6:
            end_day = week_days[(week_count + week_start) % 7]
        else:
            end_day = week_days[week_count + week_start]

    if day == 0:
        if start_day == "Not provided":
            new_time = f"{hour}:{minute} {meridiem}"
        else:
            new_time = f"{hour}:{minute} {meridiem}, {end_day}"
    else:
        if start_day == "Not provided":
            new_time = f"{hour}:{minute} {meridiem} {days_passed}"
        else:
            new_time = f"{hour}:{minute} {meridiem}, {end_day} {days_passed}"

    return new_time
