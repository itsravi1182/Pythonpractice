import os
import pandas as pd
import os
from io import StringIO
import xml.etree.ElementTree as ET
from openpyxl import Workbook, load_workbook

error_count = 0
login_count = 0
task_count = 0



folder_path = '/mnt/c/Users/10653007/OneDrive - LTI/Documents/CMA-CGM/Health_Report_automation/'  # Replace with the path to your folder

files = os.listdir(folder_path)

for file in files:
    print(file)

for file_name in files:
    if 'error' in file_name:
        suffix = int(file_name.split('error')[1].split('.')[0])
        print(f"Error pages: {suffix}")
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            contents = f.read()
        # Read the contents into a DataFrame
        df = pd.read_csv(StringIO(contents))
        # Count the number of non-empty rows in column B
        num_non_empty_rows = df['Error Time'].count()
        error_count += (suffix-1)*(100)+(num_non_empty_rows)

    if 'task' in file_name:
        suffix = int(file_name.split('task')[1].split('.')[0])
        print(f"Task pages: {suffix}")
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            contents = f.read()
        # Read the contents into a DataFrame
        df = pd.read_csv(StringIO(contents))
        # print(df.head())
        # Count the number of non-empty rows in column B
        num_non_empty_rows = df['Start Time'].count()
        task_count += (suffix-1)*(100)+(num_non_empty_rows)




    if 'Logon' in file_name:
        print("Yes Logon is there")
        print("Filesname: ",file_name)
        file_path = os.path.join(folder_path, file_name)
       

        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Get the "user" details
        users = []
        for logonActivityItem in root.findall('.//logonActivityItem'):
            user = logonActivityItem.get('user')
            users.append(user)

        #print(users)

        # Get the total count of users and the number of distinct values
        toal_users = len(users)
        distinct_users = len(set(users))

print("-----------------------------------------------")
print(f"Error_Count: {error_count}")
print(f"Task_Count: {task_count}")
print("Total number of users:", toal_users)
print("Number of distinct users:", distinct_users)
print("-----------------------------------------------")


# Load the workbook
output_file = 'scripts/HealthReport.xlsx'
file_path = os.path.join(folder_path, output_file)

workbook = load_workbook(filename= file_path)
worksheet = workbook['app_stats']


# Write the counts to the worksheet
worksheet['A2'] = distinct_users
worksheet['B2'] = toal_users
worksheet['C2'] = error_count
worksheet['D2'] = task_count

# Save the workbook
workbook.save(filename=file_path)