
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()  
X,y = load_iris(return_X_y=True)

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
iris_df["target_names"] = pd.Categorical.from_codes(iris.target, iris.target_names)


iris_df.plot.scatter('sepal length (cm)', 'sepal width (cm)', c='target')
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'])

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30, random_state=42 )
# plt.show()

print(X_train.shape)
print(X_test.shape)


# print(iris_df)