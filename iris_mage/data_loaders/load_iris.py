
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from sklearn.datasets import load_iris as sklearn_load_iris


@data_loader
def load_data(*args, **kwargs):
    iris = sklearn_load_iris(as_frame=True)
    df = iris.frame

    return df


@test
def test_output(output, *args) -> None:
    assert output is not None, 'Output is empty'
    assert len(output) == 150, 'Expected 150 rows'
    assert 'target' in output.columns, 'Target column is missing'
