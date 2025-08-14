from sklearn import linear_model
import sys
import importlib

# fmt:off
# Adjust the path to import from the parent directory
sys.path.append("../classes")

import regression_model_class as rmc

importlib.reload(rmc)
# fmt:on

regression_model = linear_model.LinearRegression()


class LinearRegressionModel(rmc.RegressionModel):
    def __init__(self):
        super().__init__(regression_model)
        print("Linear Regression model Initialized.")

    def train(self, X_train, y_train):
        super().train(X_train, y_train)

    def predict(self, X_test):
        predictions = super().predict(X_test)
        return predictions

    def evaluate(self, X_test, y_test):
        evaluation_metrics = super().evaluate(X_test, y_test)
        return evaluation_metrics
