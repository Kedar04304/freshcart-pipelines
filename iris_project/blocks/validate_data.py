@transformer
def validate_data(data, *args, **kwargs):
    df = data["data"]
    assert not df.isnull().any().any(), "Missing values found"
    assert df["target"].nunique() == 3, "Expected exactly three Iris classes"
    return {"rows": len(df), "classes": int(df["target"].nunique())}

@test
def test_validate_data(output, *args):
    assert output["rows"] == 150
    assert output["classes"] == 3
