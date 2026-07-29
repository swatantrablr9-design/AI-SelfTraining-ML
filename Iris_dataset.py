from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print(iris)
#print(X)
#print(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Detailed report
print(classification_report(y_test, y_pred))



# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

#print(iris)

print("Features:", feature_names)
print("Target classes:", iris.target_names)



# Scatter plot of Petal Length vs Petal Width
plt.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target, cmap='viridis')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris Dataset: Petal Dimensions')
plt.colorbar(label='Species')
plt.show()


# Scatter plot of Sepal Length vs Sepal Width
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target, cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset: Sepal Dimensions')
plt.colorbar(label='Species')
plt.show()