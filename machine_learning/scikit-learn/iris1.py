from sklearn.datasets import load_iris

iris = load_iris()  
# ou
X,y = load_iris(return_X_y=True)
iris.target[[10,25,50]]

print(list(iris.target_names))
print(iris.target)
print(iris.data)