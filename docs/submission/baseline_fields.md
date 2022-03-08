# Baseline Fields: Measures collected only at baseline 
----------
## **Record and linkage Fields**
----------

 ---------

 
### Jcoin Data Commons Person Identifier


**Variable name:** ```jdc_person_id```

**Description:** The generated unique identifier specific to the JCOIN Data Commons for a given individual (client or staff).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

----------
## **Enrollment Fields**
----------

 ---------

 
### Quarter Enrolled


**Variable name:** ```quarter_enrolled```

**Description:** The financial quarter and year of enrollment

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### State Of Site For Enrollment


**Variable name:** ```state_of_site_enrollment```

**Description:** The U.S. State abbreviation of the site where client (participant) was initially enrolled

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Current Study Status


**Variable name:** ```current_study_status```

**Description:** A summary of the current status where client (participant) is in study

**Variable type:** String

**Possible values:** On study,Dropped out,Withdrawn by investigator,Completed study

**Required:** Yes

----------
## **Demographics Fields**
----------

 ---------

 
### Gender Identity 


**Variable name:** ```o2 ```

**JCOIN Core Measure Question Text:** What is your gender identity? 


**Description:** Gender identity 


**Variable type:** String

**Possible values:** Male,Female,Transgender man/trans man/female-to-male (FTM),Transgender woman/trans woman/male-to-female (MTF),Genderqueer/gender nonconforming/neither exclusively male nor female,Additional gender category (or other),Not reported

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.] 
False if not 'Male' and not 'Transfgender' else True
 ---------

 
### Gender Identity (Condensed)


**Variable name:** ```d4b```

**JCOIN Core Measure Question Text:** What is your gender identity? 


**Description:** A condensed version of the gender identity common data element 


**Variable type:** String

**Possible values:** Male,Female,Transgender,Gender nonconforming,Something else,Not reported

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.] 
 ---------

 
### Race: White


**Variable name:** ```d3_white```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** Denotes person with European, Middle Eastern, or North African ancestral origin who identifies, or is identified, as White.


**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Black Or African American


**Variable name:** ```d3_black```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** A person having origins in any of the Black racial groups of Africa. Terms such as "Haitian" or "Negro" can be used in addition to "Black or African American". (OMB)

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: American Indian Or Alaska Native


**Variable name:** ```d3_american_indian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** Denotes a person having origins in one of the indigenous peoples of North America, who lived on the continent prior to the European colonization. The term includes individuals belonging to a large number of tribes, states, and ethnic groups, many of them still enduring as communities.


**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Native Hawaiian Or Other Pacific Islander


**Variable name:** ```d3_hawaiian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** Denotes a person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. The term covers particularly people who identify themselves as part-Hawaiian, Native Hawaiian, Guamanian or Chamorro, Carolinian, Samoan, Chuukese (Trukese), Fijian, Kosraean, Melanesian, Micronesian, Northern Mariana Islander, Palauan, Papua New Guinean, Pohnpeian, Polynesian, Solomon Islander, Tahitian, Tokelauan, Tongan, Yapese, or Pacific Islander, not specified.


**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Asian


**Variable name:** ```d3_asian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. (OMB)

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Other


**Variable name:** ```d3_other```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** A person having origins in a race not identified with other racial categories presented


**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: American Indian Principal Tribe Or Community Specified


**Variable name:** ```d3_specify_tribe```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** The specific principal tribe or community if the person answered answered 'yes' to this racial category


**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Race: Other Specified


**Variable name:** ```d3_specify_other```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY


**Description:** The specific racial category of a person having origins in a race not identified with other racial categories presented


**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Hispanic, Latino, Or Spanish Origin


**Variable name:** ```d2```

**JCOIN Core Measure Question Text:** Are you of Hispanic, Latino, or Spanish origin?

**Description:** A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes