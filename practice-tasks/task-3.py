from datetime import datetime
import pytz

### Showing current date and time
current = datetime.now()
formatted_current = current.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {formatted_current}")

### Days until a future date input by user
while True:
    try:
        user_input = input("Enter a future date (YYYY-MM-DD): ")
        future = datetime.strptime(user_input, "%Y-%m-%d").date()
        today = datetime.today().date()
        if future < today:
            print("Past date entered")
        else:
            difference = future - today
            break
    except ValueError:
        print("Invalid Date Format")
        
print(f"Days until {future}: {difference.days} days")

### Difference between 2 user input times
while True:
    try:
        t1_input = input("Enter 1st time: ")
        t2_input = input("Enter 2nd time: ")

        t1 = datetime.strptime(t1_input, "%H:%M:%S")
        t2 = datetime.strptime(t2_input, "%H:%M:%S")

        if t1>t2:
            print(t1-t2)
            break
        else:
            print(t2-t1)
            break
            
    except ValueError:
        print("Invalid Time Format")

###Showing current time in UTC in UTC, US/Eastern and Asia/Kolkata regions
utc_zone = pytz.utc
utc_time = datetime.now(utc_zone)

eastern_zone = pytz.timezone('US/Eastern')
eastern_time = utc_time.astimezone(eastern_zone)

kolkata_zone = pytz.timezone('Asia/Kolkata')
kolkata_time = utc_time.astimezone(kolkata_zone)
    
print(f"Current time in UTC: {utc_time.strftime("%H:%M:%S")}")
print(f"Current time in US/Eastern: {eastern_time.strftime("%H:%M:%S")}")
print(f"Current time in Asia/Kolkata: {kolkata_time.strftime("%H:%M:%S")}")