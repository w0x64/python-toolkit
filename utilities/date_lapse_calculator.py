import re
from datetime import datetime

def calculate_offline_time(input_str):
    # Regex to find YYYY-MM-DD HH:MM:SS anywhere in the string
    date_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    match = re.search(date_pattern, input_str)
    
    if not match:
        print("❌ No valid date found in the input.")
        return
    
    date_str = match.group(1)
    
    try:
        last_online = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("❌ Could not parse the date, please check the format.")
        return
    
    now = datetime.now()
    
    # Calculate months and remaining days
    months = (now.year - last_online.year) * 12 + (now.month - last_online.month)
    # Adjust if the current day is less than the last_online day
    if now.day < last_online.day:
        months -= 1

    # Calculate remaining days/hours/minutes/seconds after removing full months
    temp_date = last_online.replace(year=last_online.year + months // 12, month=(last_online.month + months % 12 -1) % 12 +1)
    if temp_date > now:
        temp_date = temp_date.replace(day=now.day)
    delta = now - temp_date
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"Last online: {last_online}")
    print(f"Time offline: {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# ======= USAGE =======
while True:
    user_input = input("Paste your remote session line (or 'exit' to quit):\n")
    if user_input.lower() == "exit":
        break
    calculate_offline_time(user_input)
    print("\n" + "-"*40 + "\n")