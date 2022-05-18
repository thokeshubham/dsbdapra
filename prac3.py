import pandas as pd

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = pd.read_csv(csv_url, header = None)
data


col_names= ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
data=pd.read_csv(csv_url,names = col_names )
data


from sklearn import preprocessing

data['Species'].unique()

label_encoder = preprocessing.LabelEncoder()

data['Species']= label_encoder.fit_transform(data['Species'])

data['Species'].unique()