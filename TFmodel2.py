# Model with decision tree classifier

from tensorflow.estimator import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Flatten the grid into a 1D array
X = initial_states.reshape(-1, N*N)
y = final_states.reshape(-1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model
model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=5)

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model's performance
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
