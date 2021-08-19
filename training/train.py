from sklearn.datasets import load_iris
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle


def train_model():
    # import data
    iris = load_iris()

    # Split dataset into X and y
    X = iris.data
    y = iris.target

    # Load dataframe
    data = pd.DataFrame(X, columns=iris.feature_names)
    data['target'] = pd.DataFrame(y.reshape(-1,1), columns=["target"])
    print(data.head(5))

    # Split data for cross validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 4)

    # Create model
    model = KNeighborsClassifier(n_neighbors=1)

    # Fit model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)
    # Print accuracy
    print("ACCURACY: ", metrics.accuracy_score(y_test, y_pred))
    # Save the model
    pickle.dump(model, open('models/model.pickle', 'wb'))
    print('Model saved.')