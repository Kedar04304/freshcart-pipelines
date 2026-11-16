from mage_ai.data_preparation.decorators import data_exporter
import json
import os

@data_exporter
def save_results(data, *args, **kwargs):
    os.makedirs("iris_mage/outputs", exist_ok=True)

    results = {
        "accuracy": data["accuracy"],
        "predictions": data["predictions"]
    }

    with open("iris_mage/outputs/iris_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Results saved successfully!")
    return results
