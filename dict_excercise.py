student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}
for name,marks in student_marks.items():
    print(name,":",marks)
    if marks>=92 and marks<=100:
        print("Grade:A+")
    elif marks>=81 and marks<=91:
        print("Grade:A")
    elif marks>=71 and marks<=80:
        print("Grade:B+")
    elif marks>=61 and marks<=70:
        print("Grade:B")
    elif marks>=51 and marks<=60:
        print("Grade:C")  
    elif marks>=41 and marks<=50:
        print("Grade:D")
    else:
        print("Grade:F")
