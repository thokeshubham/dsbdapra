import pandas as pd 

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(csv_url, header = None)
iris

iris.isnull

col_names= ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
iris=pd.read_csv(csv_url,names = col_names )
iris

iris.dtypes

iris.shape

iris['Sepal_Length']

iris.sort_values("Sepal_Length",ascending=False)

print(iris[10:21])

sliced_iris=iris[10:21]
print(sliced_iris)

newcols = {"Species":"Type" }
iris.rename(columns = newcols, inplace = True)
print(iris)

newcols={
"Id":"id",

"Sepal_Width":"float",
"Sepal_Length":"float"
}

iris.rename(columns=newcols,inplace=True)

print(iris.head())

