# Time point Fields: Measures collected at all time points (baseline and follow ups)
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
 ---------

 
### Visit Number


**Variable name:** ```visit_number```

**Description:** A number that identifies the visit or timepoint of data collection (baseline=1 and each subsequent follow up is 2 or greater).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Visit Type


**Variable name:** ```visit_type```

**Description:** The visit type/category (either baseline or follow up)

**Variable type:** String

**Possible values:** Baseline,Follow-up

**Required:** Yes

----------
## **Substance Use Fields**
----------

 ---------

 
### Last Time Drug Use


**Variable name:** ```s1a```

**JCOIN Core Measure Question Text:** When was the last time you used alcohol or other drugs weekly or more often?

**Description:** Last time a person used alcohol or other drugs weekly or more often

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Getting, Using, Or Recovering


**Variable name:** ```s1b```

**JCOIN Core Measure Question Text:** When was the last time you spent a lot of time either getting alcohol or other drugs, using alcohol or other drugs, or recovering from the effects of alcohol or other drugs (feeling sick)?

**Description:** Last time a person spent a lot of time either getting alcohol or other drugs, using alcohol or other drugs, or recovering from the effects of alcohol or other drugs (feeling sick)

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Social Dysfunction


**Variable name:** ```s1c```

**JCOIN Core Measure Question Text:** When was the last time you kept using alcohol or other drugs even though it was causing social   problems, leading to fights, or getting you into trouble with other people?

**Description:** Last time a person kept using alcohol or other drugs even though it was causing social  problems, leading to fights, or getting you into trouble with other people

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Work Or Life Dysfunction


**Variable name:** ```s1d```

**JCOIN Core Measure Question Text:** When was the last time your use of alcohol or other drugs caused you to give up or reduce your involvement in activities at work, school, home or social events?

**Description:** Last time a person's use of alcohol or other drugs caused giving up or reducing involvement in activities at work, school, home or social events

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Withdrawal


**Variable name:** ```s1e```

**JCOIN Core Measure Question Text:** When was the last time you had withdrawal problems from alcohol or other drugs like shaky hands, throwing up, having trouble sitting still or sleeping, or you used any  alcohol or other drugs to stop being sick or avoid withdrawal problems?

**Description:** Last time a person had withdrawal problems from alcohol or other drugs like shaky hands, throwing up, having trouble sitting still or sleeping, or used any  alcohol or other drugs to stop being sick or avoid withdrawal problems

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Any Opioids


**Variable name:** ```s2a```

**JCOIN Core Measure Question Text:** When was the last time you used any kind of heroin, fentanyl or other opioid?(such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?

**Description:** Last time a person used any kind of heroin, fentanyl, or other opioid

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Opioid Overdose


**Variable name:** ```s2b```

**JCOIN Core Measure Question Text:** When was the last time you had an opioid overdose? [used enough of the drug that it produced a life-threatening reaction that required medical attention]

**Description:** Last time a person had an opioid overdose

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Last Time Drug Use: Oud Medication-Assisted Treatment


**Variable name:** ```s2c```

**JCOIN Core Measure Question Text:** When was the last time you went to any kind of medication assisted treatment for opioid use disorder?

**Description:** Last time a person had a medication assisted treatment for opioid use disorder

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know

**Required:** Yes
 ---------

 
### Opioid Overdose Count


**Variable name:** ```s3a```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you overdose on heroin, fentanyl or other opioids?  [Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention]

**Description:** Number of times a person overdosed on heroin, fentanyl or other opioids during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 ---------

 
### Opioid Overdose Count: Receiving Naloxone


**Variable name:** ```s3b```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you receive naloxone (Evzio or Narcan) to reverse your overdose?

**Description:** Number of times a person received naloxone (Evzio or Narcan) to reverse your overdose during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 ---------

 
### Person Who Administered Nalaxone For Overdose


**Variable name:** ```s3c```

**JCOIN Core Measure Question Text:** Who administered the naloxone or Narcan? (SELECT ALL THAT APPLY)

**Description:** People who administered naloxone or narcan

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** TODO: expand fields to each of the possible selections
 ---------

 
### Drugs 4 Hrs Before Overdose


**Variable name:** ```s3d```

**JCOIN Core Measure Question Text:** What drugs had you taken in the 4 hours before you overdosed? (SELECT ALL THAT APPLY)

**Description:** Drugs taken in the 4 hours before overdose

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** TODO: expand fields to each of the possible selections
 ---------

 
### Emergency Medical Service Following Overdose


**Variable name:** ```s3e```

**JCOIN Core Measure Question Text:** How many of these times did you receive emergency medical service following an overdose?

**Description:** Number of times a person received emergency medical service following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Emergency Department Visit Count Following Overdose


**Variable name:** ```s3f```

**JCOIN Core Measure Question Text:** How many of these times did you go to the emergency department following an overdose?

**Description:** Number of times a person went to the emergency department following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Hospital Admissions Count Following Overdose


**Variable name:** ```s3g```

**JCOIN Core Measure Question Text:** How many of these times did you get admitted to the hospital following an overdose?

**Description:** Number of times a person got admitted to the hospital following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Substance Use Treatment Referral Count Following Overdose


**Variable name:** ```s3h```

**JCOIN Core Measure Question Text:** How many of these times did you receive a referral to substance use treatment from the police, EMS, ED or hospital staff?

**Description:** Number of times a person received a referral to substance use treatment from the police, EMS, ED or hospital staff

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Drug Use Count


**Variable name:** ```s4a```

**JCOIN Core Measure Question Text:** During the 90 days (prior to entering jail or prison/since your last assessment), on how many days did you use any heroin, fentanyl, opioids, alcohol, marijuana or other illicit drugs?

**Description:** Number of times a person used any heroin, fentanyl, opioids, alcohol, marijuana or other illicit drugs  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Alcohol Use Count


**Variable name:** ```s4b```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you drink any kind of alcohol (beer, gin, rum, scotch, tequila, whiskey, wine or mixed drinks)?

**Description:** Number of times a person drank any kind of alcohol (beer, gin, rum, scotch, tequila, whiskey, wine or mixed drinks)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Alcohol Use Count: Binge Drinking


**Variable name:** ```s4c```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you have 5 or more drinks?

**Description:** Number of times a person had 5 or more drinks during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Marijuana Use Count: Medical


**Variable name:** ```s4d```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use medical marijuana that was obtained from a dispensary with your own recommendation card or prescription?

**Description:** Number of times a person used medical marijuana that was obtained from a dispensary with their own recommendation card or prescription during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Marijuana Use Count: Not Own


**Variable name:** ```s4e```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use other marijuana, including hashish, edibles, tinctures or concentrated drops, blunts or other forms of THC (cannabis, herb, pot, reefer, weed), or medical marijuana that was not your own?

**Description:** Number of times a person used other marijuana, including hashish, edibles, tinctures or concentrated drops, blunts or other forms of THC (cannabis, herb, pot, reefer, weed), or medical marijuana that was not their own

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Opioid Use Count: Heroin


**Variable name:** ```s4f```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use heroin (alone or mixed with other drugs)?

**Description:** Number of times a person used heroin (alone or mixed with other drugs) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Opioid Use Count: Fentanyl


**Variable name:** ```s4g```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use fentanyl (alone or mixed with other drugs)?

**Description:** Number of times a person used fentanyl (alone or mixed with other drugs)  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Opioid Use Count: Street Methadone


**Variable name:** ```s4h```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use nonprescription or street methadone?

**Description:** Number of times a person used nonprescription or street methadone  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Opioid Use Count: Suboxone


**Variable name:** ```s4j```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use use nonprescription or street Suboxone?

**Description:** Number of times a person used nonprescription or street Suboxone  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Opioid Use Count: Other


**Variable name:** ```s4k```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use other opioids, opiates, painkillers, or other analgesics (such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?

**Description:** Number of times a person used other opioids, opiates, painkillers, or other analgesics (such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Cocaine Use Count


**Variable name:** ```s4m```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use crack, smoked rock, freebase, or other forms of cocaine?

**Description:** Number of times a person used crack, smoked rock, freebase, or other forms of cocaine during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Speed Use Count


**Variable name:** ```s4n```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use any methamphetamines, amphetamines, or other forms of speed?

**Description:** Number of times a person used any methamphetamines, amphetamines, or other forms of speed during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Benzodiazapine, Anti-Anxiety, And Tranquilizer Use Count


**Variable name:** ```s4p```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you use any benzodiazepines, anti-anxiety drugs or tranquilizers (such as Ativan, Equanil, Dalmane, Deprol, Diazepam, Klonopin, Librium, Lortab, Meprobamate, Miltown, Prosom, Serax, Traxene, Valium, Verseed, Xanax)?

**Description:** Number of times a person used any benzodiazepines, anti-anxiety drugs or tranquilizers (such as Ativan, Equanil, Dalmane, Deprol, Diazepam, Klonopin, Librium, Lortab, Meprobamate, Miltown, Prosom, Serax, Traxene, Valium, Verseed, Xanax) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Drug Use Count: Other


**Variable name:** ```s4z```

**JCOIN Core Measure Question Text:** During the 90 days (prior to entering jail or prison/since your last assessment), on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)?

**Description:** Number of days a person use any other drug that has not been mentioned (such as hallucinogens, downers) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Drug Use: Description Of Other Drugs


**Variable name:** ```s4z_describe```

**JCOIN Core Measure Question Text:** During the 90 days(prior to entering jail or prison/since your last assessment), on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)? (Please describe )

**Description:** A description of drugs that have not been mentioned (such as hallucinogens, downers) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Place Of No Opioid Use (Jail, Hospital, Etc)


**Variable name:** ```s5```

**JCOIN Core Measure Question Text:** During the 90 days (prior to entering jail or prison/ since your last assessment), on how many days have you been in a jail, hospital or other place where you could not use heroin, fentanyl, other opioids, alcohol, marijuana or other drugs? (USE 0 FOR NONE)

**Description:** Number of days a person has been in jail, hospital, or other place where they could not use heroin, fentanyl, other opioids, alcohol, marijuana, or other drugs

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

----------
## **Justice Involvement Fields**
----------

 ---------

 
### Activities Against Law Besides Drugs


**Variable name:** ```j1a```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), on how many days were you involved in any activities that might get you into trouble or be against the law besides drug use? [IF 0, GO TO J2]

**Description:** During the past 90 days (since last assessment), on how many days were a person involved in any activities that might get a person into trouble or be against the law besides drug use? [IF 0, GO TO J2]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** [IF 0, GO TO J2]
 ---------

 
### Drug Possession


**Variable name:** ```j1a1```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  been in possession of small amounts of drugs? (drug possession)

**Description:** Number of times  a person  been in possession of small amounts of drugs? (drug possession)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Drunkenness Or Other Liquor Law Violations


**Variable name:** ```j1a2```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  been drunk or high in public? (drunkenness or other liquor law violations)

**Description:** Number of times  a person  been drunk or high in public? (drunkenness or other liquor law violations)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Driving Under The Influence Or While Intoxicated


**Variable name:** ```j1a3```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  driven a vehicle while under the influence of alcohol or drugs? (driving under the influence or while intoxicated)

**Description:** Number of times  a person  driven a vehicle while under the influence of alcohol or drugs? (driving under the influence or while intoxicated)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Possession, Dealing, Distribution Or Sale Of Drugs


**Variable name:** ```j1a4```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you …sold, distributed or helped to make illegal drugs?  (possession, dealing, distribution or sale of drugs)

**Description:** Number of times  a person …sold, distributed or helped to make illegal drugs?  (possession, dealing, distribution or sale of drugs)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Vandalism Or Property Destruction


**Variable name:** ```j1a5```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  purposely damaged or destroyed property that did not belong to you? (vandalism or property destruction)

**Description:** Number of times  a person  purposely damaged or destroyed property that did not belong to a person? (vandalism or property destruction)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Receiving, Possessing Or Selling Stolen Goods


**Variable name:** ```j1a6```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  bought, received, possessed or sold any stolen goods? (receiving, possessing or selling stolen goods)

**Description:** Number of times  a person  bought, received, possessed or sold any stolen goods? (receiving, possessing or selling stolen goods)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Forgery, Fraud Or Embezzlement


**Variable name:** ```j1a7```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  passed bad checks, forged or altered a prescription, or took money illegally from an employer?  (forgery, fraud or embezzlement)

**Description:** Number of times  a person  passed bad checks, forged or altered a prescription, or took money illegally from an employer?  (forgery, fraud or embezzlement)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Shoplifting


**Variable name:** ```j1a8```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  taken something from a store without paying for it? (shoplifting)

**Description:** Number of times  a person  taken something from a store without paying for it? (shoplifting)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Larceny Or Theft


**Variable name:** ```j1a9```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  other than from a store, taken money or property that didn't belong to you? (larceny or theft)

**Description:** Number of times  a person  other than from a store, taken money or property that didn't belong to a person? (larceny or theft)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Burglary Or Breaking And Entering


**Variable name:** ```j1a10```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  broken into a house or building to steal something or just to look around? (burglary or breaking and entering)

**Description:** Number of times  a person  broken into a house or building to steal something or just to look around? (burglary or breaking and entering)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Motor Vehicle Theft


**Variable name:** ```j1a11```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  taken a car without people in it that didn't belong to you? (motor vehicle theft)

**Description:** Number of times  a person  taken a car without people in it that didn't belong to a person? (motor vehicle theft)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Carjacking


**Variable name:** ```j1a12```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  taken a car from someone who was in it? (carjacking)

**Description:** Number of times  a person  taken a car from someone who was in it? (carjacking)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Simple Assault Or Battery


**Variable name:** ```j1a13```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  hit someone or gotten into a physical fight? (simple assault or battery)

**Description:** Number of times  a person  hit someone or gotten into a physical fight? (simple assault or battery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Robbery


**Variable name:** ```j1a14```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  used a weapon, force, or strong-arm methods to get money or things from a person? (robbery)

**Description:** Number of times  a person  used a weapon, force, or strong-arm methods to get money or things from a person? (robbery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Aggravated Assault Or Battery


**Variable name:** ```j1a15```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  hurt someone badly enough they needed bandages or a doctor? (aggravated assault or battery)

**Description:** Number of times  a person  hurt someone badly enough they needed bandages or a doctor? (aggravated assault or battery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Forcible Rape


**Variable name:** ```j1a16```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  made someone have sex with you by force when they did not want to have sex? (forcible rape)

**Description:** Number of times  a person  made someone have sex with a person by force when they did not want to have sex? (forcible rape)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Murder, Homicide Or No-Negligent Manslaughter


**Variable name:** ```j1a17```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  been involved in the death or murder of another person, including accidents? (murder, homicide or no-negligent manslaughter)

**Description:** Number of times  a person  been involved in the death or murder of another person, including accidents? (murder, homicide or no-negligent manslaughter)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Arson


**Variable name:** ```j1a18```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  intentionally set a building, car or other property on fire? (arson)

**Description:** Number of times  a person  intentionally set a building, car or other property on fire? (arson)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Prostitution, Pimping Or Commercialized Sex


**Variable name:** ```j1a19```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  traded sex for food, drugs or money? (prostitution, pimping or commercialized sex)

**Description:** Number of times  a person  traded sex for food, drugs or money? (prostitution, pimping or commercialized sex)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Other Unlawful Activities


**Variable name:** ```j1a99```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times have you  done something else that would have gotten you into trouble with the police if they had known about it? (carrying a weapon, gang involvement, domestic violence, trespass, gambling, distributing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy,  ) (PLEASE DESCRIBE)

**Description:** Number of times  a person  done something else that would have gotten a person into trouble with the police if they had known about it? (carrying a weapon, gang involvement, domestic violence, trespass, gambling, distributing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy,  ) (PLEASE DESCRIBE)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Overall Charged Arrests


**Variable name:** ```j2```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times were you arrested and charged?

**Description:** Number of a times person was arrested and charged

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Drug Possession Arrests


**Variable name:** ```j2a```

**JCOIN Core Measure Question Text:** Number of arrests for drug possession (for small amounts)

**Description:** Number of arrests for drug possession (for small amounts)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Law Violations Arrests


**Variable name:** ```j2b```

**JCOIN Core Measure Question Text:** Number of arrests for drunkenness or other liquor law violations

**Description:** Number of arrests for drunkenness or other liquor law violations

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Driving Under The Influence/Intoxicated Arrests


**Variable name:** ```j2c```

**JCOIN Core Measure Question Text:** Number of arrests for driving under the influence or while intoxicated

**Description:** Number of arrests for driving under the influence or while intoxicated

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Drug Activity Arrests


**Variable name:** ```j2d```

**JCOIN Core Measure Question Text:** Number of arrests for possession, dealing, distribution or sale of drugs

**Description:** Number of arrests for possession, dealing, distribution or sale of drugs

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Vandalism Or Property Destruction Arrests


**Variable name:** ```j2e```

**JCOIN Core Measure Question Text:** Number of arrests for vandalism or property destruction

**Description:** Number of arrests for vandalism or property destruction

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Stolen Goods Arrests


**Variable name:** ```j2f```

**JCOIN Core Measure Question Text:** Number of arrests for receiving, possessing or selling stolen goods

**Description:** Number of arrests for receiving, possessing or selling stolen goods

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Forgery, Fraud Or Embezzlement Arrests


**Variable name:** ```j2g```

**JCOIN Core Measure Question Text:** Number of arrests for forgery, fraud or embezzlement

**Description:** Number of arrests for forgery, fraud or embezzlement

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Shoplifting Arrests


**Variable name:** ```j2h```

**JCOIN Core Measure Question Text:** Number of arrests for shoplifting

**Description:** Number of arrests for shoplifting

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Theft/Larceny Arrests


**Variable name:** ```j2i```

**JCOIN Core Measure Question Text:** Number of arrests for larceny or theft

**Description:** Number of arrests for larceny or theft

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Burglary Or Breaking And Entering Arrests


**Variable name:** ```j2j```

**JCOIN Core Measure Question Text:** Number of arrests for burglary or breaking and entering

**Description:** Number of arrests for burglary or breaking and entering

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Vehicle Theft Arrests


**Variable name:** ```j2k```

**JCOIN Core Measure Question Text:** Number of arrests for motor vehicle theft

**Description:** Number of arrests for motor vehicle theft

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Car Jacking Arrests


**Variable name:** ```j2l```

**JCOIN Core Measure Question Text:** Number of arrests for car jacking

**Description:** Number of arrests for car jacking

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Simple Assault Or Battery Arrests


**Variable name:** ```j2m```

**JCOIN Core Measure Question Text:** Number of arrests for simple assault or battery

**Description:** Number of arrests for simple assault or battery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Robbery Arrests


**Variable name:** ```j2n```

**JCOIN Core Measure Question Text:** Number of arrests for robbery

**Description:** Number of arrests for robbery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Aggravated Assault Or Battery Arrests


**Variable name:** ```j2o```

**JCOIN Core Measure Question Text:** Number of arrests for aggravated assault or battery

**Description:** Number of arrests for aggravated assault or battery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Forcible Rape Arrests


**Variable name:** ```j2p```

**JCOIN Core Measure Question Text:** Number of arrests for forcible rape

**Description:** Number of arrests for forcible rape

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Negligent Manslaughter Arrests


**Variable name:** ```j2q```

**JCOIN Core Measure Question Text:** Number of arrests for murder, homicide or non-negligent manslaughter

**Description:** Number of arrests for murder, homicide or non-negligent manslaughter

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Arson Arrests


**Variable name:** ```j2r```

**JCOIN Core Measure Question Text:** Number of arrests for arson

**Description:** Number of arrests for arson

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Commercialized Sex Arrests


**Variable name:** ```j2s```

**JCOIN Core Measure Question Text:** Number of arrests for prostitution, pimping or commercialized sex

**Description:** Number of arrests for prostitution, pimping or commercialized sex

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Other Charges Arrests


**Variable name:** ```j2t```

**JCOIN Core Measure Question Text:** Number of arrests for other charges (carrying a weapon, gang involvement, domestic violence, trespass, gambling, disturbing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy)

**Description:** Number of arrests for other charges (carrying a weapon, gang involvement, domestic violence, trespass, gambling, disturbing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Electronic Monitoring


**Variable name:** ```j3a```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been  on electronic monitoring?

**Description:** Number of days person has been on electronic monitoring

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### House Arrest


**Variable name:** ```j3b```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been  on house arrest?

**Description:** Number of days a person has been on house arrest

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Jail Time


**Variable name:** ```j3c```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been  in jail?

**Description:** Number of days a person has been in jail

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Prison Time


**Variable name:** ```j3d```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been  in prison?

**Description:** Number of days a person has been in prison

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Current Jail Or Prison


**Variable name:** ```j3e```

**JCOIN Core Measure Question Text:** Are you currently in jail or prison? (CAN MARK IF OBVIOUS)

**Description:** Person is currently in jail or prison

**Variable type:** String

**Possible values:** Yes,No

**Required:** Yes
 ---------

 
### Length Of Jail Or Prison Time


**Variable name:** ```j3f```

**JCOIN Core Measure Question Text:** How long have you been in jail or prison? (just this episode)

**Description:** Length of jail or prison time for this episode

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Parole


**Variable name:** ```j4a```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been on parole?

**Description:** Number of days a person has been on parole

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Probation


**Variable name:** ```j4b```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been on probation?

**Description:** Number of days a person has been on probation

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Other Kind Of Community Supervision


**Variable name:** ```j4c```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been on any other kind of community supervision?

**Description:** Number of days a person has been on any other kind of community supervision

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Meeting With Probation Or Parole Officer


**Variable name:** ```j4d```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you met with your probation or parole officer?

**Description:** Number of days a person has met with a probation or parole officer

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Trouble With Probation Or Parole Officer


**Variable name:** ```j4e```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many days have you been in trouble with your probation or parole officer?

**Description:** Number of days a person has been in trouble with a probation or parole officer

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Life Time Arrests


**Variable name:** ```j5a```

**JCOIN Core Measure Question Text:** During your lifetime, how many times in your life have you been arrested including as a juvenile?

**Description:** Number of days a person has been arrested in their lifetime (including juvenile)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### First Time Arrest


**Variable name:** ```j5b```

**JCOIN Core Measure Question Text:** During your lifetime, how old were you the first time you were arrested?

**Description:** Age at time of first arrest

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Lifetime Years In Detention, Jail, Or Prison Time


**Variable name:** ```j5c_years```

**JCOIN Core Measure Question Text:** During your lifetime, how much total time have you spent in detention, jail or prison during your lifetime?

**Description:** Number of times a person has spent in detention, jail or prison during a personr lifetime?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Lifetime Months In Detention, Jail, Or Prison Time


**Variable name:** ```j5c_months```

**JCOIN Core Measure Question Text:** During your lifetime, how much total time have you spent in detention, jail or prison during your lifetime?

**Description:** Number of times a person has spent in detention, jail or prison during lifetime

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Lifetime Guity And Sentenced


**Variable name:** ```j5d```

**JCOIN Core Measure Question Text:** During your lifetime, how many times have you been found guilty and sentenced (including adjudications as a youth or convictions as an adult)?

**Description:** Number of times a person has been found guilty and sentenced (including adjudications as a a personth or convictions as an adult)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### First Time Adjudication Conviction


**Variable name:** ```j5e```

**JCOIN Core Measure Question Text:** During your lifetime, how old were you the first time you were adjudicated or convicted?

**Description:** Age at which a person was first adjudicated and convicted

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes