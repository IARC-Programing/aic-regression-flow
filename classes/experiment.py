import pandas as pd
from sklearn.model_selection import train_test_split


class Experiment():
    def __init__(self, model, experiment_name=None):
        self.model = model
        self.dataset = None
        self.experiment_name = experiment_name
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_dataset(self, data_path):
        self.dataset = pd.read_csv(data_path)
        print(f"Dataset loaded from {data_path}")

    def preprocess_data(self, test_size=0.2, random_state=42, target_column='target', input_columns=None):
        # Placeholder for data preprocessing logic
        # This should include handling missing values, encoding categorical variables, etc.
        if self.dataset is not None:
            # Example preprocessing step: splitting dataset into features and target
            if input_columns is not None:
                X = self.dataset[input_columns]
            else:
                X = self.dataset.drop(target_column, axis=1)
            y = self.dataset[target_column]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state)
            print("Data preprocessing completed.")
        else:
            raise ValueError(
                "Dataset is not loaded. Please load the dataset first.")

    def run_experiment(self, epochs=10, batch_size=32):
        error_list = pd.DataFrame(columns=['epoch', 'mse', 'r2'])
        if self.dataset is None:
            raise ValueError(
                "Dataset is not loaded. Please load the dataset first.")

        # Placeholder for running the experiment
        # This should include training the model, making predictions, and evaluating performance
        print(f"Running experiment '{self.experiment_name}'")

        # For every epoch
        for epoch in range(epochs):
            # For every samples in batches
            print(f"Training epoch {epoch + 1}/{epochs}...")
            error_mse = 0.0  # Placeholder for error metric
            error_r2 = 0.0  # Placeholder for error metric
            for i in range(0, len(self.X_train), batch_size):
                X_batch = self.X_train[i:i + batch_size]
                y_batch = self.y_train[i:i + batch_size]
                # Here we would typically call a method to train the model on this batch
                # For example: self.model.train(X_batch, y_batch)
                self.model.train(X_batch, y_batch)

            # After training on all batches, we could evaluate the model
            if self.X_test is not None and self.y_test is not None:
                evaluation = self.model.evaluate(self.X_test, self.y_test)
                print(f"Evaluation after epoch {epoch + 1}: {evaluation}")
                error_mse += evaluation['mse']
                error_r2 += evaluation['r2']
            else:
                print("No test data available for evaluation.")
            # Optionally, we could save the model after each epoch
            # self.model.export_model(f"model_epoch_{epoch + 1}.pkl")
            # For demonstration, we will just print the epoch completion

            # Summarizing the epoch error
            epoch_error_mse = error_mse / \
                len(self.X_train) if len(self.X_train) > 0 else 0
            epoch_error_r2 = error_r2 / \
                len(self.X_train) if len(self.X_train) > 0 else 0
            print(
                f"Epoch {epoch + 1} completed. MSE: {epoch_error_mse}, R2: {epoch_error_r2}")
            print(f"Epoch {epoch + 1}/{epochs} completed.")
            error_list_payload = {
                'epoch': epoch + 1,
                'mse': epoch_error_mse,
                'r2': epoch_error_r2
            }
            error_list = pd.concat([error_list, pd.DataFrame(
                [error_list_payload])], ignore_index=True)

        print("Experiment completed.")
        self.model.export_model(f"{self.experiment_name}_final_model.pkl")
        return error_list
