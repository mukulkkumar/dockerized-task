from datetime import datetime
import pandas as pd

start_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 1 Started at {start_date_time_stamp}")

student_details =('student_details.xlsx')
student_data = pd.read_excel(student_details)
print(student_data)

end_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 1 Completed at {end_date_time_stamp}")
