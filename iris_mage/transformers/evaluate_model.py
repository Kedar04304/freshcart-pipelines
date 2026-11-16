from mage_ai.data_preparation.decorators import transformer, test
from sklearn.metrics import accuracy_score, classification_report

@transformer
def evaluate_model(data, *args, **kwargs):
    predictions = data["model"].predict(data["X_test"])
    accuracy = accuracy_score(data["y_test"], predictions)

    print("Model accuracy:", accuracy)
    print(classification_report(data["y_test"], predictions))

    return {
        "accuracy": accuracy,
        "predictions": predictions.tolist()
    }

@test
def test_output(output, *args):
    assert 0 <= output["accuracy"] <= 1
    assert len(output["predictions"]) == 30
