"""Test date and time related functions."""

import pytest

def test_datetime_format_string_regex():
    """Test the regular expressions for each unique permutation of the
    datetime format string, as defined in the dateTimeFormatString_regex.csv"""

    # Read the CSV file with the 