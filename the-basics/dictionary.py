#! /usr/bin/python3

student_grades = {"Batman":9.0, "Superman":9.5, "Deadpool": 7.5}

sum_of_grades = sum(student_grades.values())
print("Sum of Grades: ", sum_of_grades)

no_of_students = len(student_grades)
print("No of students: ", no_of_students)

average_of_grades = sum_of_grades / no_of_students

print("Average Grade: ", average_of_grades)