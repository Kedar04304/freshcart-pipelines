import pandas as pd

@data_exporter
def save_results(data, *args, **kwargs):
    pd.DataFrame({"actual": data["y_test"].to_numpy(),
                  "predicted": data["predictions"]}).to_csv(
                      "iris_predictions.csv", index=False
                  )
    return {"csv_path": "iris_predictions.csv",
            "accuracy": data["accuracy"], "max_depth": data["max_depth"]}
