from sklearn.datasets import load_iris
import pandas as pd

@data_loader
def load_iris_data(*args, **kwargs):
    data = load_iris(as_frame=True)
    df = data.frame
    df = df.rename(columns={"target": "target"})
    return {"data": df, "feature_columns": list(data.feature_names),
            "target_column": "target", "target_names": list(data.target_names)}
