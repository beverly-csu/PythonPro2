import pandas as pd

df = pd.read_csv('train.csv')


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


def count_langs(langs):
    return len(langs.split(';'))


def know_english(langs):
    langs = langs.split(';')
    if 'English' in langs:
        return 1
    else:
        return 0


def fix_sex(sex):
    return sex - 1


def fill_career_start(career_start):
    if career_start == 'False':
        return 2009
    elif career_start == '666':
        return 2009
    else:
        return int(career_start)


def fill_career_end(career_end):
    if career_end == 'False':
        return 2013
    else:
        return int(career_end)


df['occupation_type'].fillna('university', inplace=True)
df['education_form'].fillna('Full-time', inplace=True)

df['sex'] = df['sex'].apply(fix_sex)
df['education_status'] = df['education_status'].apply(fix_education_status)
df['know english'] = df['langs'].apply(know_english)
df['count langs'] = df['langs'].apply(count_langs)
df['career_start'] = df['career_start'].apply(fill_career_start)
df['career_end'] = df['career_end'].apply(fill_career_end)

df[list(pd.get_dummies(df['education_form']).columns)
   ] = pd.get_dummies(df['education_form'])
df[list(pd.get_dummies(df['occupation_type']).columns)
   ] = pd.get_dummies(df['occupation_type'])

df = df.drop(['bdate', 'education_form', 'langs', 'life_main', 'people_main',
             'city', 'last_seen', 'occupation_type', 'occupation_name'], axis=1)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x = df.drop('result', axis=1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifer = KNeighborsClassifier(n_neighbors=11)
classifer.fit(x_train, y_train)

y_pred = classifer.predict(x_test)
accuracy = accuracy_score(y_test, y_pred) * 100
print(round(accuracy, 1), '%')