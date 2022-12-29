# создай здесь свой индивидуальный проект!
import pandas as pd

df = pd.read_csv('train.csv')


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


def make_ed_form(form):
    if form == 'Distance Learning':
        return 1
    elif form == 'Part-time':
        return 2
    else:
        return 0


def know_english(langs):
    langs = langs.split(';')
    if 'English' in langs:
        return 1
    else:
        return 0


def check_occ_type(occupation_type):
    if occupation_type == 'work':
        return 0
    else:
        return 1


df['has_mobile'] = df['has_mobile'].apply(int)
df['followers_count'] = df['followers_count'].apply(int)
df['education_status'] = df['education_status'].apply(make_ed_status)
df['education_form'] = df['education_form'].apply(make_ed_form)
df['relation'] = df['relation'].apply(int)
df['english'] = df['langs'].apply(know_english)
df['occupation_type'] = df['occupation_type'].apply(check_occ_type)

df = df.drop(['id', 'city', 'people_main', 'bdate', 'graduation', 'life_main',
             'langs', 'last_seen', 'occupation_name', 'career_start', 'career_end'], axis=1)


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

classifer = KNeighborsClassifier(n_neighbors=3)
classifer.fit(x_train, y_train)

y_pred = classifer.predict(x_test)
print(accuracy_score(y_test, y_pred) * 100, '%')