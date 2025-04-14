"""Test date and time related functions."""

import csv
import re
import pytest
from pathlib import Path

# Path to the CSV file
CSV_FILE_PATH = (
        Path(__file__).parent.parent /
        "practices/dateTimeFormatString/dateTimeFormatString_regex.csv")

def load_csv_data(file_path):
    """
    Load data from the specified CSV file.
    The file is expected to have rows in the format:
    [format_string, example_value, regex]
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [row for row in reader if row]  # Skip empty rows
    return data

@pytest.mark.parametrize("row", load_csv_data(CSV_FILE_PATH))
def test_datetime_format(row):
    """
    Test that the regex in the third column matches the example date/time
    value in the second column.
    """
    format_string, example_value, regex = row
    assert re.match(regex, example_value), (f"Regex '{regex}' did not match "
                                            f"value '{example_value}' for "
                                            f"format '{format_string}'")


if __name__ == "__main__":
    # Run the tests if this script is executed directly
    pytest.main([__file__])