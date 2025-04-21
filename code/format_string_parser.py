#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: format_string_parser

:Synopsis:
    Reads a list of datetime format strings and generates regular expressions
:Author:
    Duane Costa

:Created:
    4/3/2018
"""

import csv
from docopt import docopt
import logging
from parsimonious.nodes import Node, NodeVisitor
from parsimonious.grammar import Grammar
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z',
                    level=logging.INFO)

logger = logging.getLogger('format_string_parser')


class FormatStringFormatter(NodeVisitor):
    """Visitor that turns a parse tree into a regular expression"""

    def visit_validDateTime(self, node, visited_children):
        return '^' + ''.join(visited_children) + '$'

    def visit_monthBasedDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayBasedDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayBasedDateReversedDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_yearDayMonthDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthYearDayDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthDayYearDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayMonthYearDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayYearMonthDateTime(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthBasedDate(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthBasedDate(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayBasedDate(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayBasedDateReversed(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthYearDay(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayYearMonth(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthDayYear(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayMonthYear(self, node, visited_children):
        return ''.join(visited_children)

    def visit_monthYearDate(self, node, visited_children):
        return ''.join(visited_children)

    def visit_yearDayMonth(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeNoMinutesNoOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeNoMinutesWithOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeNoSecondsNoOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeNoSecondsWithOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeNoOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeWithOffset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_time(self, node, visited_children):
        return ''.join(visited_children)

    def visit_timeZ(self, node, visited_children):
        return ''.join(visited_children)

    def visit_year(self, node, visited_children):
        return r'(\d\d\d\d)'

    def visit_month(self, node, visited_children):
        return r'(01|02|03|04|05|06|07|08|09|10|11|12)'

    def visit_yearMonth(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayOfMonth(self, node, visited_children):
        return r'(0[1-9]|[1-2]\d|30|31)'

    def visit_dateDash(self, node, visited_children):
        return node.text

    def visit_timeColon(self, node, visited_children):
        return node.text

    def visit_T(self, node, visited_children):
        return node.text

    def visit_hours(self, node, visited_children):
        return r'([0-1]\d|2[0-4])'

    def visit_minutes(self, node, visited_children):
        return r'([0-5]\d)'

    def visit_wholeSeconds(self, node, visited_children):
        return r'([0-5]\d)'

    def visit_fractionalSeconds(self, node, visited_children):
        return r'(\.\d\d\d)'

    def visit_secondsWithFraction(self, node, visited_children):
        return ''.join(visited_children)

    def visit_secondsWithOutFraction(self, node, visited_children):
        return ''.join(visited_children)

    def visit_seconds(self, node, visited_children):
        return ''.join(visited_children)

    def visit_dayOfYear(self, node, visited_children):
        return r'[0-3]\d\d'

    def visit_offsetOperator(self, node, visited_children):
        return '\\' + node.text

    def visit_offset(self, node, visited_children):
        return ''.join(visited_children)

    def visit_offsetHours(self, node, visited_children):
        return ''.join(visited_children)

    def visit_offsetHoursMinutes(self, node, visited_children):
        return ''.join(visited_children)

    def visit_Z(self, node, visited_children):
        return node.text


def format_string_visitor(format_string):
    grammar = Grammar(
        """
        validDateTime = monthBasedDateTime / dayBasedDateTime / 
                        yearDayMonthDateTime /  monthYearDayDateTime / 
                        dayYearMonthDateTime / 
                        monthDayYearDateTime /
                        dayMonthYearDateTime /
                        dayBasedDateReversedDateTime /
                        yearDayMonth /
                        dayMonthYear / 
                        monthYearDay /
                        monthDayYear /
                        dayYearMonth /
                        monthYearDate /                        
                        monthBasedDate / 
                        dayBasedDate / 
                        dayBasedDateReversed /
                        yearMonth / 
                        year / 
                        timeZ
        monthBasedDateTime = monthBasedDate T time Z
        dayBasedDateTime = dayBasedDate T time Z
        dayBasedDateReversedDateTime = dayBasedDateReversed T time Z
        yearDayMonthDateTime = yearDayMonth T time Z
        monthYearDayDateTime = monthYearDay T time Z
        dayYearMonthDateTime = dayYearMonth T time Z
        monthDayYearDateTime = monthDayYear T time Z
        dayMonthYearDateTime = dayMonthYear T time Z
        
        monthBasedDate = year dateDash month dateDash dayOfMonth
        dayBasedDate = year dateDash dayOfYear
        dayBasedDateReversed = dayOfYear dateDash year
        yearDayMonth = year dateDash dayOfMonth dateDash month
        monthYearDay = month dateDash year dateDash dayOfMonth
        dayYearMonth = dayOfMonth dateDash year dateDash month
        monthDayYear = month dateDash dayOfMonth dateDash year
        dayMonthYear = dayOfMonth dateDash month dateDash year
        monthYearDate = month dateDash year
        
        timeNoMinutesNoOffset = hours
        timeNoMinutesWithOffset = hours offset
        timeNoSecondsNoOffset = hours timeColon minutes
        timeNoSecondsWithOffset = hours timeColon minutes offset
        timeNoOffset = hours timeColon minutes timeColon seconds
        timeWithOffset = hours timeColon minutes timeColon seconds offset
        time = timeWithOffset / timeNoOffset / timeNoSecondsWithOffset / \
               timeNoSecondsNoOffset / timeNoMinutesWithOffset / \
               timeNoMinutesNoOffset
        timeZ = time Z
        
        year = "YYYY"
        month = "MM"
        yearMonth = year dateDash month
        dayOfMonth = ~r"(?!DDD)DD"
        dateDash = ~"[-/]?"
        timeColon = ~":?"
        T = ~r"[T\s]?"
        hours = "hh"
        minutes = "mm"
        wholeSeconds = "ss"
        fractionalSeconds = ".sss"
        secondsWithFraction = wholeSeconds fractionalSeconds
        secondsWithOutFraction = wholeSeconds
        seconds = secondsWithFraction / secondsWithOutFraction
        dayOfYear = "DDD"
        offsetOperator = ~r"[+-]"
        offset = offsetHoursMinutes / offsetHours
        offsetHours = offsetOperator hours
        offsetHoursMinutes = offsetOperator hours timeColon minutes
        Z = ~"Z?"   
        """)

    tree = grammar.parse(format_string)
    result = FormatStringFormatter().visit(tree)
    return result


def main():
    """
    Reads a list of datetime format strings and generates regular expressions
    corresponding to each format string.

    Usage:
        format_string_parser.py [-i | --input <input>]
                                [-o | --output <output>]
        format_string_parser.py -h | --help

    Options:
        -i --input    Input file to read format strings from
        -o --output   Output results to file;
                      the filename should have a .csv extension
        -h --help     This page

    """
    args = docopt(str(main.__doc__))
    input = args['<input>']
    output = args['<output>']

    if input is None:
        fin = sys.stdin
    else:
        fin = open(input, 'rt')

    if output is None:
        fout = sys.stdout
    else:
        fout = open(output, 'wt')

    format_strings = fin.readlines()

    if (input):
        fin.close()

    for line in format_strings:
        stripped_line = line.strip()
        line_parts = stripped_line.split(',')
        format_string = line_parts[0]
        logger.info("Parsing %s" % format_string)
        regex_result = format_string_visitor(format_string)
        output_line = "%s,%s\n" % (stripped_line, regex_result)
        fout.write(output_line)

    if (output):
        fout.close()

    logger.info("Finished program")


def diff_datetime_format_lists(path1, path2):
    """
    Compare two CSV files containing datetime format strings and return
    the differences between them.

    :param path1: Path to the first CSV file.
    :param path2: Path to the second CSV file.
    """
    with open(path1, mode="r", encoding="utf-8") as file1, \
         open(path2, mode="r", encoding="utf-8") as file2:
        reader1 = csv.reader(file1)
        reader2 = csv.reader(file2)

        # Create set of values in first column of reader2
        reader2_set = {row[0] for row in reader2}

        # compare the first item in each row of reader1 against reader2_set
        # and return if matches
        diff = [row[0] for row in reader1 if row[0] not in reader2_set]

        return diff


if __name__ == "__main__":
    main()