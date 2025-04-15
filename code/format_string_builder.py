"""Date and Time Format String Generator

This script generates a list of date and time format strings and their
corresponding example date strings. These formats are based on EDI's
definitions of acceptable date and time formats
(https://github.com/PASTAplus/PEP/blob/main/peps/pep-4.md).
"""

import csv
import re
from itertools import permutations
from pathlib import Path


def generate_date_formats() -> list:
    """
    Generates a list of date format strings based on EDI's definitions
    of acceptable date formats.

    :returns: A list of format strings for all permutations of year, month,
        and day components.
    """
    components = ["YYYY", "MM", "DD"]
    separators = ["", "/", "-"]
    format_strings = []

    for perm in permutations(components):
        for sep in separators:
            format_string = f"{perm[0]}{sep}{perm[1]}{sep}{perm[2]}"
            format_strings.append(format_string)

    # Additional dates not composable in the above way
    format_strings.extend([
        "YYYYDDD",
        "YYYY/DDD",
        "YYYY-DDD",
        "DDDYYYY",
        "DDD/YYYY",
        "DDD-YYYY"
    ])

    return format_strings


def generate_datetime_formats() -> list:
    """
    Generates a list of date and time format strings based on EDI's definitions
    of acceptable date and time formats.

    :returns: A list of format strings for all permutations of date, time,
        and timezone components.
    """
    date_formats = generate_date_formats()
    time_formats = [
        "hh",
        "hhmm",
        "hhmmss",
        "hhmmss.sss",
        "hh:mm",
        "hh:mm:ss",
        "hh:mm:ss.sss",
    ]
    timezone_formats = [
        "Z",
        "+hh:mm",
        "+hhmm",
        "+hh",
        "-hh:mm",
        "-hhmm",
        "-hh"
    ]
    date_and_time_separators = ["T", " "]

    formats = []

    # Add date components
    formats.extend(date_formats)

    # Generate combinations of date and time components
    for date_component in date_formats:
        for time_component in time_formats:
            if time_component:
                for separator in date_and_time_separators:
                    for tz_component in timezone_formats:
                        formats.append(
                            f"{date_component}{separator}{time_component}{tz_component}")
            else:
                formats.append(date_component)

    # Additional specific formats
    formats.extend(["YYYY-MM", "YYYYMM", "MMYYYY", "MM-YYYY", "YYYY"])

    return formats


def generate_example_date(format_string: str) -> str:
    """
    Generates an example date string based on the provided format string.

    :param format_string: The format string to generate an example date and time value
        for.
    :return: An example date string based on the provided format.
    """

    example_date_time = {
        "YYYY": "1976",
        "MM": "09",
        "DDD": "267",
        "DD": "23",
        "hh": "11",
        "mm": "11",
        "sss": "888",
        "ss": "11",
        "Z": "Z",
        "+hh:mm": "+07:30",
        "+hhmm": "+0730",
        "+hh": "+07",
        "-hh:mm": "-07:30",
        "-hhmm": "-0730",
        "-hh": "-07"
    }

    for key, value in example_date_time.items():
        format_string = format_string.replace(key, value)

    return format_string


def write_to_csv(formats: list, file_path: str) -> None:
    """
    Writes the generated date and time format strings and their example
    date strings to a CSV file.

    :param formats: A list of date and time format strings.
    :param file_path:  The path to the CSV file to write the format strings to.
    :return: None
    """
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for _, format in enumerate(formats):
            example_date = generate_example_date(format)
            csv_writer.writerow([format, example_date])


def main(csv_file_path: str) -> None:
    """
    Main function to generate date and time format strings and write them
    to a CSV file.

    :param csv_file_path: The path to the CSV file to write the format strings
        to.
    :return: None
    """
    formats = generate_datetime_formats()
    write_to_csv(formats, csv_file_path)
    print(
        f"CSV file '{csv_file_path}' has been generated with date and time format strings.")


if __name__ == "__main__":

    CSV_FILE_PATH = Path(__file__).parent.parent / "practices/dateTimeFormatString/dateTimeFormatString_list.csv"
    main(str(CSV_FILE_PATH))