# EML Congruence Checker

The EML Congruence Checker (ECC) acts as the 'gatekeeper' for datasets entering the PASTA repository. The checks themselves are designed by the data management community. The group talks weekly, over Zoom.

# Current activities
## checks
* dateTimeFormatString (planned to be in production Nov 2017). For more info, see /practices/
* dateTimeFormat conguence (planned to be in production Nov 2017). For more info, see /practices/
## PASTA behavior related to checks
* checksum optimization (opt in with a query parameter). link to more info here: TBD

# Repository contents
## <> Code (directories)
### archive
holds a cached version of the cannonical list of checks, which is a dynamic doc (google spreadsheet). 

### practices
holds check-specific details and notes 

because 'best practice' drives code design (and vice versa), there will be some text here that relates to BP. But this is not the location for BP recommendations. 

### meetings
holds meeting notes and agendas, as necessary. The agenda for the next call is in the dir's README.


## Other repository areas
### Wiki
Documentation about the ECC itself, e.g., 
* working group products, eg reports, papers
* how-tos 
* links out to BP recommendations.

### Issues
* TO DOs for the ECC working group
* suggested new checks from the community
