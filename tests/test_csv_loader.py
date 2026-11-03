import pandas as pd
import pytest

from etp_inflow_forecasting.ingestion.csv_loader import load_csv


def test_load_csv(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text(
        "date,value\n2026-01-01,100\n",
        encoding="utf-8",
    )

    result = load_csv(file_path)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.loc[0, "value"] == 100


def test_load_csv_missing_file(tmp_path):
    file_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_csv(file_path)
