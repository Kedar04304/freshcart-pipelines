from mage_ai.data_preparation.decorators import transformer, test
from sklearn.tree import DecisionTreeClassifier

@transformer
def train_model(data, *args, **kwargs):
    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(data["X_train"], data["y_train"])

    return {
        "model": model,
        "X_test": data["X_test"],
        "y_test": data["y_test"]
    }

@test
def test_output(output, *args):
    assert output["model"] is not None
    assert len(output["X_test"]) == 30
