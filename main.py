from backend import get_four_day_weather

forecast = get_four_day_weather()

for day in forecast:
    
    if len(day) == 5:
        date_str, weather, emoji, temp, air_quality = day
        print(f"{date_str}: {weather} {emoji}, {temp}, Air Quality: {air_quality}")
    else:
        date_str, weather, emoji, temp = day
        print(f"{date_str}: {weather} {emoji}, {temp}")
