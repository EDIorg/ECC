"""Date and Time Format String Generator

This script generates a list of date and time format strings and their
corresponding example date strings. These formats are based on EDI's
recommended set of date and time format strings.
"""


import csv
from itertools import permutations


def generate_date_formats() -> list:
    """
    :returns: A list of format strings for all permutations of date year,
        month, and day components.
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
        "DDD-YYYY",
    ])

    return format_strings


def generate_datetime_formats():
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
    formats.extend(["YYYY-MM", "YYYYMM", "MMYYYY", "MM-YYYY"])

    return formats


def generate_example_date(format):
    example = "1976-09-23"
    example_time = "11:11:11.888"
    example_yyyymmdd = "19760923"
    example_yyyyd = "1976-250"
    example_yyyyd_dd = "1976250"

    example_date_time = {
        "YYYY": "1976",
        "MM": "09",
        "DD": "23",
        "hh": "11",
        "mm": "11",
        "ss": "11",
        "sss": "888",
        "Z": "Z",
        "+hh:mm": "+07:30",
        "+hhmm": "+0730",
        "+hh": "+07",
        "-hh:mm": "-07:30",
        "-hhmm": "-0730",
        "-hh": "-07"
    }

    for key, value in example_date_time.items():
        format = format.replace(key, value)

    return format


def write_to_csv(formats, file_path):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for _, format in enumerate(formats):
            example_date = generate_example_date(format)
            csv_writer.writerow([format, example_date])


def main():
    formats = generate_datetime_formats()
    csv_file_path = '/Users/csmith/Data/ecc/dateTimeFormatString_list.csv'
    write_to_csv(formats, csv_file_path)
    print(
        f"CSV file '{csv_file_path}' has been generated with date and time format strings.")


if __name__ == "__main__":
    main()