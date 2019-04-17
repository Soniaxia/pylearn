lilei = {
    "name":"Lilei",
    "homework":[90,97,75,92],
    "quizzes":[88,40,94],
    "tests":[75,90]
}
hanmeimei = {
    "name":"Hanmeimei",
    "homework":[100,92,98,100],
    "quizzes":[82,83,91],
    "tests":[89,97]
}
jim = {
    "name":"Jim",
    "homework":[0,87,75,22],
    "quizzes":[0,75,78],
    "tests":[100,100]
}

students = [lilei,hanmeimei,jim]

# for student in students:
#     for key,value in student.items():
#         print(key,value)

def average(number):
    total=sum(number)
    average=total/len(number)
    return average

def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    total_average=homework*0.1+quizzes*0.3+tests*0.6
    return total_average

def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

def get_class_average(class_list):
    results=[]
    for student in class_list:
        results.append(get_average(student))
    class_average=average(results)
    return class_average

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))