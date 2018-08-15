# Meetings

Directory holds meeting material. If you add meeting notes, please put your name and date in filename. add the agenda at the top of the file.  Readme should hold agenda of next call.

# Next call: TBD
## Agenda


These are some notes Margaret saved from a slack conversations. do we have an issue here? 


### quotes in date
Stevan Earl [16:34]
so, this is interesting, because the date values in the data set are quoted, maybe?
```'"2012-03-29"' is not congruent with the formatString 'YYYY-MM-DD' as specified in the metadata. regex: ^(\d\d\d\d)-(01|02|03|04|05|06|07|08|09|10|11|12)-(0[1-9]|[1-2]\d|30|31)$```

Duane Costa [16:36]
yep, the quotes would cause the regex to fail. i wonder, is this the appropriate response?

Stevan Earl [16:37]
yeah, not sure, it is a bit misleading. I wonder if that is something that our group should discuss next time we meet? Can you have different messages depending on the type of error found?

Duane Costa [16:39]
off hand, i don't think so. really, all the checker can say is that the regex failed, but really no way of knowing how or why
if quotes are used commonly, i suppose we could go the extra step of checking for them and issuing that the checker spotted this issue as part of the error message


Note (mob): EML has a quoteCharacter, for CSV handling -- eg, you might choose to export a csv with all "string fields quoted". so it would impact every field, not just dates. Does the DML use the quoteCharacter? and if so, what for?
Note (another one): move this to an issue, not an agenda item
