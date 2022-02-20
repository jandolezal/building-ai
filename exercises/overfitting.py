"""
Exercise 19: Looking out for overfitting

https://buildingai.elementsofai.com/Machine-Learning/overfitting
"""


# Intermediate

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

ks = [1, 42, 100, 250]

for k in ks:
    # Create a classifier and fit it to our data
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    train_acc = knn.score(x_train, y_train)

    print(f"k={k: <4} training accuracy: %f" % train_acc)
    test_acc = knn.score(x_test, y_test)
    print(f"k={k: <4} testing accuracy: %f" % test_acc)


# Advanced

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)


def clasify(k=1):
    # Create a classifier and fit it to our data
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    print("training accuracy: %f" % knn.score(x_train, y_train))
    print("testing accuracy: %f" % knn.score(x_test, y_test))


ks = [1, 42, 100, 250]

for k in ks:
    clasify(k)
