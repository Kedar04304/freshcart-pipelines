import pandas as pd
from sklearn.model_selection import train_test_split


def test_prepare_data():
    iris = pd.DataFrame({
        "feature1": range(150),
        "target": [0, 1, 2] * 50
    })

    X = iris[["feature1"]]
    y = iris["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    assert len(X_train) == 121
    assert len(X_test) == 30
