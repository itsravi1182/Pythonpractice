
from clw_func import read_csv_to_dataframes
from Metric import Metric

file_path = folder_path = '/mnt/c/Users/10653007/OneDrive - LTI/Documents/CMA-CGM/Health_Report_automation/'

avg_file = "avg.csv"
max_file = "max.csv"

avg_data = read_csv_to_dataframes(file_path, avg_file)
max_data = read_csv_to_dataframes(file_path, max_file)

# Loop through DataFrame rows
for index, row in avg_file.iterrows():
    column1_value = row['Column1']
    instance_id = row['Column1'].split("InstanceId:")[1].split()[0]
    print(f"Row {index}: Column1 = {column1_value}, InstanceId = {instance_id}")




instance_id = "12345"
cpu_usage = 80.0
memory_usage = 70.0
cdisk_usage = 50.0
ddisk_usage = 60.0

metric_object = Metric(instance_id, cpu_usage, memory_usage, cdisk_usage, ddisk_usage)







