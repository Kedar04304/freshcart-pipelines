from mage_ai.data_preparation.decorators import transformer, test
from sklearn.model_selection import train_test_split


@transformer
def prepare_data(df, *args, **kwargs):
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test
    }


@test
def test_output(output, *args):
    assert len(output["X_train"]) == 120
    assert len(output["X_test"]) == 30
    assert len(output["y_train"]) == 120
    assert len(output["y_test"]) == 30
