"""Date and Time Format String Generator

This script generates a list of date and time format strings and their
corresponding example date strings. These formats are based on EDI's
recommended set of date and time format strings.
"""


import csv
from itertools import permutations

def generate_date_components():
    components = ["YYYY", "MM", "DD"]
    separators = ["", "/", "-"]
    format_strings = []

    # Generate permutations of the components
    for perm in permutations(components):
        # Generate combinations with consistent separators
        for sep in separators:
            format_string = f"{perm[0]}{sep}{perm[1]}{sep}{perm[2]}"
            format_strings.append(format_string)

    return format_strings



def generate_date_formats():
    # Define basic date and time components
    # date_components = [
    #     "YYYY-MM-DD",
    #     "YYYYMMDD",
    #     "YYYY-DDD",
    #     "YYYYDDD"
    # ]
    date_components = generate_date_components()
    time_components = ["hh:mm:ss.sss", "hh:mm:ss", "hhmmss.sss", "hhmmss",
                       "hh:mm", "hhmm", "hh", ""]
    timezone_components = ["Z", "+hh:mm", "+hhmm", "+hh", "-hh:mm", "-hhmm",
                           "-hh", ""]
    separators = ["T", " "]

    formats = []

    # Generate combinations of date and time components
    for date_component in date_components:
        for time_component in time_components:
            if time_component:
                for separator in separators:
                    for tz_component in timezone_components:
                        formats.append(
                            f"{date_component}{separator}{time_component}{tz_component}")
            else:
                formats.append(date_component)

    # Add additional formats without separators
    for date_component in date_components:
        for time_component in time_components:
            if time_component:
                for tz_component in timezone_components:
                    formats.append(
                        f"{date_component}{time_component}{tz_component}")

    # Additional specific formats
    formats.extend([
        "YYYY-MM", "YYYYMM"
    ])

    return formats


def generate_example_date(format):
    example = "1976-09-23"
    example_time = "11:11:11.888"
    example_day = "250"
    example_yyyymmdd = "19760923"
    example_yyyyd = "1976-250"
    example_yyyyd_dd = "1976250"

    example_date_time = {
        "YYYY": "1976",
        "MM": "09",
        "DD": "23",
        "DDD": example_day,
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
        for i, format in enumerate(formats):
            example_date = generate_example_date(format)
            csv_writer.writerow([i + 1, format, example_date])


def main():
    formats = generate_date_formats()
    csv_file_path = '/Users/csmith/Data/ecc/dateTimeFormatString_list.csv'
    write_to_csv(formats, csv_file_path)
    print(
        f"CSV file '{csv_file_path}' has been generated with date and time format strings.")


if __name__ == "__main__":
    main()