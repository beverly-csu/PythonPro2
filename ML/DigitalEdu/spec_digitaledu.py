import pandas as pd

df = pd.read_csv('train.csv')


def fix_sex(sex):
    return sex - 1


df['sex'] = df['sex'].apply(fix_sex)


def fix_education_status(education_status):
    if education_status == 'Undergraduate applicant':
        return 0
    elif education_status == "Student (Bachelor's)":
        return 1
    elif education_status == "Alumnus (Bachelor's)":
        return 2
    elif education_status == "Student (Master's)":
        return 3
    elif education_status == "Alumnus (Master's)":
        return 4
    elif education_status == "Student (Specialist)":
        return 5
    elif education_status == "Alumnus (Specialist)":
        return 6
    elif education_status == 'PhD':
        return 7
    elif education_status == 'Candidate of Sciences':
        return 8


df['education_status'] = df['education_status'].apply(fix_education_status)

def fix_occupation_type(occupation_type):
    if occupation_type == 'work':
        return occupation_type
    else:
        return 'university'


df['occupation_type'] = df['occupation_type'].apply(fix_occupation_type)


def fix_langs(langs):
    langs = langs.split(';')
    if 'English' in langs:
        return 1
    else:
        return 0


df['langs'] = df['langs'].apply(fix_langs)

df['education_form'].fillna('Full-time', inplace=True)

df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df[list(pd.get_dummies(df['occupation_type']).columns)] = pd.get_dummies(df['occupation_type'])

df = df.drop(['id', 'bdate', 'relation', 'life_main', 'people_main', 'city', 'last_seen',
             'occupation_name', 'career_start', 'career_end', 'occupation_type', 'education_form'], axis=1)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = df.drop('result', axis=1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifer = KNeighborsClassifier()
classifer.fit(x_train, y_train)

y_pred = classifer.predict(x_test)
accuracy = accuracy_score(y_test, y_pred) * 100

print(f'Точность работы модели = {accuracy}%')