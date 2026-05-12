"""Tests for BCIM parametrization data files (JSON and CSV formats)."""
import json
from pathlib import Path
from pydantic import ValidationError
import pytest
import pandas as pd
import sys

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf.bcim.parametrization import InputData  # noqa
from simdesign.rcmrf.bcim.parametrization import ArchetypeData  # noqa


@pytest.fixture
def all_json_data() -> dict:
    """Load JSON data from all parameter files and return it as a dict."""
    data_path = Path(__file__).parents[1]
    data_path = data_path / 'simdesign' / 'rcmrf' / 'bcim' / 'data'
    json_files = list(data_path.glob('*.json'))
    all_json_data = {}
    for file in json_files:
        with open(file, 'r') as json_file:
            all_json_data[file.name] = json.load(json_file)
    return all_json_data


def test_json_format(all_json_data: dict) -> None:
    """Check that all JSON parameter files conform to the InputData schema."""
    for filename, json_data in all_json_data.items():
        try:
            InputData(**json_data)
        except ValidationError as e:
            assert False, f"JSON file '{filename}' has incorrect format: {e}"


@pytest.fixture
def all_csv_data() -> pd.DataFrame:
    """Load CSV data from layouts.csv and return it as a DataFrame."""
    data_path = Path(__file__).parents[1]
    data_path = data_path / 'simdesign' / 'rcmrf' / 'bcim' / 'data'
    file_path = data_path / 'layouts.csv'
    csv_data = pd.read_csv(file_path)
    return csv_data


def test_csv_format(all_csv_data: pd.DataFrame) -> None:
    """Check that each row in layouts.csv conforms to the ArchetypeData schema.
    """
    for _, row in all_csv_data.iterrows():
        try:
            ArchetypeData(**row.to_dict())
        except ValidationError as e:
            assert False, f"layouts.csv file has incorrect format: {e}"
