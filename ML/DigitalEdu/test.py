import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('train_clear.csv')
df_t = pd.read_csv('test_clear.csv')

x = df.drop('result', axis=1)
y = df['result']

sc = StandardScaler()
x = sc.fit_transform(x)
x_test = sc.transform(df_t)

classifer = KNeighborsClassifier(n_neighbors=3)
classifer.fit(x, y)

df_t['result'] = classifer.predict(x_test)
print(df.head(10))