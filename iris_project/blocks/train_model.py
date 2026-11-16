from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import os

@test
def test_model_accuracy(output, *args):
    assert 0.0 <= output["accuracy"] <= 1.0

@transformer
def train_model(data, *args, **kwargs):
    runtime_vars = kwargs.get("runtime_vars", {}) or {}
    max_depth = int(runtime_vars.get("max_depth", 3))
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(data["X_train"], data["y_train"])
    predictions = model.predict(data["X_test"])
    accuracy = accuracy_score(data["y_test"], predictions)
    return {"model": model, "predictions": predictions,
            "accuracy": float(accuracy), "y_test": data["y_test"],
            "max_depth": max_depth, "feature_columns": data["feature_columns"],
            "target_names": data["target_names"]}
