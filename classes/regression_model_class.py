import pickle
from sklearn.metrics import mean_squared_error, r2_score


class RegressionModel:
    def __init__(self, model):
        self.model = model

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return {"mse": mse, "r2": r2}

    def export_model(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)
            print(f"Model exported to {file_path}")

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)
            print(f"Model loaded from {file_path}")
