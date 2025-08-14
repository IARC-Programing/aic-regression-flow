import sys
import importlib

# fmt:off
sys.path.append("..")
from model import linear_regression as rrg
from classes import experiment as exp
importlib.reload(rrg)
importlib.reload(exp)
# fmt:on


def main():
    test_linear_experiment = exp.Experiment(
        experiment_name="Test Linear Regression Experiment",
        model=rrg.LinearRegressionModel()
    )

    test_linear_experiment.load_dataset("example_dataset.csv")

    test_linear_experiment.preprocess_data(
        test_size=0.2,
        random_state=42,
        target_column='average_number',
        input_columns=['year']
    )

    test_linear_experiment.run_experiment(
        epochs=10,
        batch_size=32
    )


main()
