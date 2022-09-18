from datetime import datetime
import time

start_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 3 Started at {start_date_time_stamp}")
time.sleep(5)
end_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 3 Completed at {end_date_time_stamp}")
