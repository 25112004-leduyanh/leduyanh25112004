minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds

kilometers = 10
km_per_mile = 1.61
total_miles = kilometers / km_per_mile

seconds_per_mile = total_seconds / total_miles
pace_minutes = int(seconds_per_mile // 60)
pace_seconds = int(seconds_per_mile % 60)

total_hours = total_seconds / 3600
speed_mph = total_miles / total_hours
