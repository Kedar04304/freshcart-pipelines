from sklearn.model_selection import train_test_split

@test
def test_train_test_sizes(output, *args):
    assert len(output["X_train"]) == 120
    assert len(output["X_test"]) == 30

@transformer
def prepare_data(data, *args, **kwargs):
    df = data["data"]
    feature_columns = data["feature_columns"]
    target_column = data["target_column"]
    X = df[feature_columns]
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    return {"X_train": X_train, "X_test": X_test,
            "y_train": y_train, "y_test": y_test,
            "feature_columns": feature_columns,
            "target_names": data["target_names"]}
