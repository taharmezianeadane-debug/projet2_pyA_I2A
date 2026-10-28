import numpy as np 
import pandas as pd 
##faire des stat 
def statistique(student):
    mean_avg = student["Average"].mean()
    maximum_avg = student["Average"].max()
    minimum_avg = student["Average"].min()
    std_avg = student["Average"].std()
    mean_age = student["Age"].mean()
    median_avg = student["Average"].median()

    return mean_avg, maximum_avg, minimum_avg, std_avg, mean_age, median_avg
##ecrire dans le fichiertxt
def save_text(mean_avg, maximum_avg, minimum_avg, std_avg, mean_age, median_avg, file_student):
    with open(file_student, "w", encoding="utf-8") as fs:
        fs.write(
            f"La moyenne : {mean_avg:.2f}\n"
            f"Le maximum : {maximum_avg:.2f}\n"
            f"Le minimum : {minimum_avg:.2f}\n"
            f"L'écart-type : {std_avg:.2f}\n"
            f"L'âge moyen : {mean_age:.2f}\n"
            f"La médiane : {median_avg:.2f}\n"
        )