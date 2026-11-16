from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

@transformer
def evaluate_model(data, *args, **kwargs):
    cm = confusion_matrix(data["y_test"], data["predictions"])
    report = classification_report(data["y_test"], data["predictions"],
                                   target_names=data["target_names"],
                                   output_dict=True)
    metrics = pd.DataFrame(report).transpose()
    metrics.to_csv("iris_metrics.csv", index=True)
    return {"confusion_matrix": cm.tolist(),
            "metrics": metrics, "metrics_path": "iris_metrics.csv"}
