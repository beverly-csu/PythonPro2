#создай здесь свой индивидуальный проект!
import pandas as pd

df = pd.read_csv('train.csv')
df.info()
print(df['education_status'].value_counts())

def make_ed_status(status):
    if status == 'Undergraduate applicant':
        return 0
    elif status == "Student (Bachelor's)":
        return 1
    elif status == 'Student (Specialist)':
        return 2
    elif status == "Student (Master's)":
        return 3
    elif status == "Alumnus (Bachelor's)":
        return 4
    elif status == 'Alumnus (Specialist)':
        return 5
    elif status == "Alumnus (Master's)":
        return 6
    elif status == 'PhD':
        return 7
    elif status == 'Candidate of Sciences':
        return 8