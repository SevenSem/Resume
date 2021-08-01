import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import preprocessing,tree
import io 



col_names = ['Gender','Age','Openness','Neuroticism','Conscientiousness','Agreeableness','Extroversion','Personality']
df = pd.read_csv(('training_dataset.csv'),header=None,names=col_names,skiprows=[0]) 
df.head()

df.Gender[df.Gender == 'M'] = 1
df.Gender[df.Gender == 'F'] = 0
feature_cols = ['Gender','Age','Openness','Neuroticism','Conscientiousness','Agreeableness','Extroversion']
X = df[feature_cols] # Features
y = df.Personality # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print(clf.predict([[0,12,5,2,7,8,9]]))

