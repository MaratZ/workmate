import argparse
import csv
from tabulate import tabulate
from typing import List, Dict, Union, Optional


def read_csv(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Чтение CSV-файла и возврат данных в виде списка словарей."""
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def apply_filter(data, filter_condition):
    if not filter_condition:
        return data

    # Разделяем по первому '=', затем удаляем пробелы вокруг оператора
    column, condition = filter_condition.split("=", maxsplit=1)
    op_value = condition.strip().split(maxsplit=1)

    if len(op_value) == 1:
        op = "=="  # Если оператор не указан, считаем "=="
        value = op_value[0]
    else:
        op, value = op_value

    filtered_data = []
    for row in data:
        row_value = row[column]
        try:
            row_num = float(row_value)
            value_num = float(value)
            condition_met = (
                    (op == ">" and row_num > value_num)
                    or (op == "<" and row_num < value_num)
                    or (op == "==" and row_num == value_num)
            )
        except ValueError:
            condition_met = op == "==" and row_value.strip() == value.strip()

        if condition_met:
            filtered_data.append(row)

    return filtered_data

def apply_aggregation(
    data: List[Dict[str, Union[str, float]]],
    agg_condition: str,
) -> Optional[Dict[str, float]]:
    """Агрегация данных (avg, min, max) по числовой колонке."""
    if not agg_condition:
        return None

    column, agg_func = agg_condition.split("=")
    numeric_values = []

    for row in data:
        try:
            numeric_values.append(float(row[column]))
        except ValueError:
            raise ValueError(f"Column '{column}' contains non-numeric values.")

    if not numeric_values:
        return None

    if agg_func == "avg":
        result = sum(numeric_values) / len(numeric_values)
    elif agg_func == "min":
        result = min(numeric_values)
    elif agg_func == "max":
        result = max(numeric_values)
    else:
        raise ValueError(f"Unknown aggregation function: {agg_func}")

    return {"function": agg_func, "column": column, "result": result}


def main():
    parser = argparse.ArgumentParser(description="Process CSV file with filtering and aggregation.")
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument("--where", help="Filter condition (e.g., 'price=> 100')", default="")
    parser.add_argument("--aggregate", help="Aggregation condition (e.g., 'price=avg')", default="")
    args = parser.parse_args()

    data = read_csv(args.file_path)

    if args.where:
        data = apply_filter(data, args.where)

    if args.aggregate:
        agg_result = apply_aggregation(data, args.aggregate)
        if agg_result:
            print(f"{agg_result['function']}({agg_result['column']}) = {agg_result['result']:.2f}")
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()