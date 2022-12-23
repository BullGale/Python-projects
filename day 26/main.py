# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie']
#
# import random
#
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
#
# stu_scores = {student_scores}
# passed_students = {student:score for (student, score) in stu_scores if score >= 60}
# print(passed_students)
data_dict = {
  "student": ["Angela", "James", "Lily"],
  "scores": [53,76,82]
}
import pandas

student = pandas.DataFrame(data_dict)
print(student)

for (index, row) in student.iterrows():
    print(index)