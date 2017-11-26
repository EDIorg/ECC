# Best practices for datetime and dateTime/formatString (DRAFT)

#### Authors: ECC working group
#### Date: 2017-06-22T11:50-07

## Summary: 
This doc has recommendations for constructing date times for EML datasets, both format strings and data values.

## Rationale:
Consistent dates and times are crucial for data integration
There are international standards for datetimes; datasets should use them.
PASTA has two checks, (1) confirm that the dateTime/formatString is from an approved list, and 
(2) confirm that datetime values adhere to the asserted dateTime/formatString (for strings in the approved list)

## Recommendations
- Dates and times should be in ISO format (see below for rules).
- Include a time zone when including a time.

### ISO rules:
In dates, no separator or one separator:”-”
In times, no separator or “:” between “hh”, “mm”, and “ss” fields and decimal point “.” for decimal seconds.
Use “T” to separate times from dates.
Use “Z” to assert that datetime is in zulu time (0-meridian, or GMT) 
Time-zone offsets: 
“+” and ‘-’ and hour, or hour and minute

Valid date time formats are a combination of date, time, and timezone strings. 

#### Date format strings:

- YYYY-MM-DD
- YYYY
- YYYYMMDD
- YYYY-MM
- YYYYMM
- YYYY-DDD
- YYYYDDD

#### Time format strings:

- hh:mm:ss.sss
- hhmmss.sss
- hh:mm:ss
- hhmmss
- hh:mm
- hhmm
- hh

#### Time zone format strings:

- Z
- +hh:mm
- +hhmm
- +hh
- -hh:mm
- -hhmm
- -hh

#### Rules for combining date, time, and timezone:

If reporting a date without time, select one of the date format strings. If reporting a date and time, select one date and one time format string and combine with a single space (e.g. "YYYY-MM-DD hh:mm:ss") or with a "T" (e.g. "YYYY-MM-DDThh:mm:ss"). If reporting a date and time, it is recommended that a time zone specifier be appended without a space (e.g.  "YYYY-MM-DDThh:mm-hh:mm"). Time zone "Z" denotes UTC, and time zone "+" or "-" are times ahead and behind UTC, respectively.

#### Examples of dateTime/formatStrings and congruence:

Format string (metadata)
Compliant data value
Non compliant data values
YYYY-MM-DDThh:mm:ss-hh

2017-06-22T11:50:11-07
2017-06-22T11:50:11-7 (time zone offset has no 0)
2017-06-22 11:50:11-7 (time-separator in format string is missing from value)

## Other information
Description of pasta checks
* Preferred Format check: this checks that the dateTimeFormatString is in the preferred (recommended) list
* Congruence check: congruence is the agreement of the dateTimeFormatString in metadata and the values in the data table itself. The congruence check may operate against a broader list of formats than just those in the preferred list (action and list of dateTimeFormatStrings whose congruence can be checked is still to be confirmed by working group)
