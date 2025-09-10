import random 

student_scores = {"Harry":81,"Ron":78,"Hermione":99, "Draco":74, "Neville":62,}
student_grades={}
print(student_scores["Harry"])
for student, score in student_scores.items():
    if score >= 60 and score <= 69:
         student_grades[student]='Fail'
    elif score >=70 and score <=79:
         student_grades[student]='Acceptable'    
    elif score >=80 and score <=89:
        student_grades[student]='Exceeds Expectations'
    elif score >=90 and score <=100:
        student_grades[student]='Outstanding'
    elif score<0 :
        pass

print(student_grades)