import csv

def write_into_csv(info_list):
      with open("student_info.csv","a",newlines="") as csv_file:
            writer= csv.writer(csv_file)
            
            writer.writerow(["Name:","Age:","Contact number:","Email ID:"])
            writer.writerow(info_list)

condition = True

while condition:

