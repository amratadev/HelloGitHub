student_data=[
       {
           "Name":"Ram",
           "roll_no":10,
           "age":20,
           "course":"Python"
       },
       {
           "Name":"Mohan",
           "roll_no":20,
           "age":22,
           "course":"Java",
           "phone_no":[8695757,6574]
       }
]
def add_new_student(name,rollno,age,course_opted):
 new_student={}
 new_student["Name"]=name
 new_student["roll_no"]=rollno
 new_student["age"]=age
 new_student["course"]=course_opted
 student_data.append(new_student)

add_new_student("Shyam",22,18,"C++")
print(student_data)