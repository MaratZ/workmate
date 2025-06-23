import pytest
from csv_processor import read_csv, apply_filter, apply_aggregation
import os
import csv


@pytest.fixture
def sample_csv(tmp_path):
    """Создаем временный CSV-файл для тестов."""
    file_path = os.path.join(tmp_path, "test.csv")
    data = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return file_path


def test_read_csv(sample_csv):
    data = read_csv(sample_csv)
    assert len(data) == 3
    assert data[0]["name"] == "iphone"


def test_filter_gt(sample_csv):
    data = read_csv(sample_csv)
    filtered = apply_filter(data, "price=> 500")
    assert len(filtered) == 2


def test_filter_eq_str(sample_csv):
    data = read_csv(sample_csv)
    filtered = apply_filter(data, "brand==apple")  # Убрали пробел после ==
    assert len(filtered) == 1


def test_aggregate_avg(sample_csv):
    data = read_csv(sample_csv)
    result = apply_aggregation(data, "price=avg")
    assert result["result"] == pytest.approx(799.0, 0.1)


def test_aggregate_min(sample_csv):
    data = read_csv(sample_csv)
    result = apply_aggregation(data, "price=min")
    assert result["result"] == 199.0