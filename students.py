import pandas as pd 
import numpy as np 
import random 
## generate ID : 
def id_generator(): 
    id=random.sample(range(1,120),10)
    return id 

## generate birth date : 
def birth_date_generator(): 
    year = random.randint(2000, 2007)
    month = random.randint(1, 12)
    
    if month == 2: 
        # la condition bissextile :
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
            day = random.randint(1, 29)
        else: 
            day = random.randint(1, 28)
    else:
        if month in [4, 6, 9, 11]: 
            day = random.randint(1, 30)
        else: 
            day = random.randint(1, 31)

    birth_date = [day, month, year]
    return birth_date

##generate age : 
def age_generator(birth_date):
    if birth_date[1] < 10:
        age = 2026 - birth_date[2]
    else:
        if birth_date[1] == 10 and birth_date[0] > 28:
            age = 2026 - birth_date[2] - 1
        else:
            age = 2026 - birth_date[2]

    return age

## grade generate: 
def grade_generator():
    grade=np.zeros(3)
    for i in range(3):
        grade[i]=random.randint(0,20)
    avrege=np.average(grade)

    return grade , avrege


def generate_student():
    students = []
    ID = id_generator()

    for i in range(10):
        Date_de_naissance = birth_date_generator()
        Age = age_generator(Date_de_naissance)
        Grade, Avg = grade_generator()

        student = {
            "ID": ID[i],
            "Date_de_naissance": Date_de_naissance,
            "Age": Age,
            "Grades": Grade,
            "Average": Avg
        }

        students.append(student)
        df_student=pd.DataFrame(students)

    return df_student


         
