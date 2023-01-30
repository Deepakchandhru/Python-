import csv

def write_into_csv(info_list):
      with open("student_info.csv","a") as csv_file:
            writer= csv.writer(csv_file)
            
            writer.writerow(["Name:","Age:","Contact number:","Email ID:"])
            writer.writerow(info_list)

condition = True

while condition:
      student_info= input("Enter students information in the following order(Name, Age, Contact number,Email ID):")
      print("Entered information:"+ student_info)

      student_info_list=student_info.split(' ')
      print("Entered split up list:"+str(student_info_list))

      write_into_csv(student_info_list)

      condition_check=input("Enter(Yes/No), if you want to continue for next student?")
      if condition_check == "Yes":
            condition = True
      elif condition_check == "No":
            condition = False
