from datetime import datetime
import pandas as pd

start_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 2 Started at {start_date_time_stamp}")

# dictionary of data
dct = {
    'ID': {
            0: 23, 1: 43, 2: 12, 
            3: 13, 4: 67, 5: 89, 
            6: 90, 7: 56, 8: 34
        },
    'Name': {
        0: 'Ram', 1: 'Deep', 
        2: 'Yash', 3: 'Aman', 
        4: 'Arjun', 5: 'Aditya', 
        6: 'Divya', 7: 'Chalsea', 
        8: 'Akash' 
    },
    'Marks': {
        0: 89, 1: 97, 2: 45, 3: 75, 
        4: 56, 5: 76, 6: 100, 7: 87, 
        8: 81
    }, 
    'Grade': {
        0: 'B', 1: 'A', 2: 'F', 3: 'C', 
        4: 'E', 5: 'C', 6: 'A', 7: 'B', 
        8: 'B'
    } 
}

# forming dataframe
data = pd.DataFrame(dct) 

# storing into the excel file
data.to_excel("/tmp/output.xlsx")
print("Output file is created successfully.")

end_date_time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Task 2 Completed at {end_date_time_stamp}")
