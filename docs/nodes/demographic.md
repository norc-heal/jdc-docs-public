# Demographic Variables

Data for the characterization of the participant by means of segementing the population (e.g., characterization by age, sex, or race).


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Variable Name</th>
      <th>Description</th>
      <th>Possible Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>D4a</td>
      <td>What was your sex at birth?</td>
      <td>Male<br>Female</td>
    </tr>
    <tr>
      <td>D4b</td>
      <td>What is your gender identity?</td>
      <td>Male<br>Female<br>Transgender<br>Gender nonconforming<br>Not reported</td>
    </tr>
    <tr>
      <td>D4c</td>
      <td>Sexual Orientation. Do you think of yourself as . . .</td>
      <td>Straight or heterosexual<br>Lesbian or gay<br>Bisexual<br>Queer, pansexual, and/or questioning<br>Something else (SPECIFY _________)</td>
    </tr>
    <tr>
      <td>D4c_specify</td>
      <td>Sexual Orientation. Do you think of yourself as . . .not matching one of the enumerated racial categories.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>D4d</td>
      <td>Have you ever been pregnant?</td>
      <td>Never been pregnant<br>Currently pregnant<br>Previously pregnant, had a child<br>Previously pregnant, did not have a child</td>
    </tr>
    <tr>
      <td>D5</td>
      <td>What is your marital status?</td>
      <td>Married [GO TO D6]<br>Widowed<br>Divorced<br>Separated<br>Never married</td>
    </tr>
    <tr>
      <td>D5a</td>
      <td>Are you currently living as married with a romantic partner?</td>
      <td>Yes, I am living as married with partner<br>No, I am not living as married with partner</td>
    </tr>
    <tr>
      <td>D6</td>
      <td>What is the highest grade or level of school you have completed or the highest degree you have received?</td>
      <td>Did not complete high school. HIGHEST GRADE COMPLETED ________<br>GED or equivalent<br>Regular high school diploma<br>Some college credit, but less than 1 year of college credit<br>1 or more years of college credit, but no degree<br>Associate’s Degree (e.g., AA or AS)<br>Graduate degree (MSW, MA, MS, JD, MD, DSW, EdD, Ph.D, etc.)<br>Other (specify)</td>
    </tr>
    <tr>
      <td>D6_1</td>
      <td>HIGHEST GRADE COMPLETED</td>
      <td>string</td>
    </tr>
    <tr>
      <td>D6_2</td>
      <td>What is the highest grade or level of school you have completed or the highest degree you have received, not matching one of the enumerated categories.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>Death_records_using_admin_data</td>
      <td>tbd</td>
      <td>string</td>
    </tr>
    <tr>
      <td>O1</td>
      <td>What sex was originally listed on your birth certificate?</td>
      <td>Male<br>Female<br>Decline to answer</td>
    </tr>
    <tr>
      <td>O2_2_gender_identity_specify</td>
      <td>Additional gender category (or other)</td>
      <td>string</td>
    </tr>
    <tr>
      <td>O2_gender_identity</td>
      <td>Do you think of yourself as...</td>
      <td>Male<br>Female<br>Transgender man/trans man/female-to-male (FTM)<br>Transgender woman/trans woman/male-to-female (MTF)<br>Genderqueer/gender nonconforming/neither exclusively male nor female<br>Additional gender category (or other)<br>Not reported</td>
    </tr>
    <tr>
      <td>age</td>
      <td>About how old are you?</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>created_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>date_and_cause_of_death_per_ICD_10_codes</td>
      <td>tbd</td>
      <td>string</td>
    </tr>
    <tr>
      <td>electronic_health_record</td>
      <td>tbd</td>
      <td>string</td>
    </tr>
    <tr>
      <td>gender</td>
      <td>What is your gender identity?</td>
      <td>Male<br>Female<br>Transgender<br>Gender nonconforming<br>Something else<br>Not reported</td>
    </tr>
    <tr>
      <td>hispanic</td>
      <td>Are you of Hispanic, Latino, or Spanish origin?</td>
      <td>Yes<br>No<br>Not reported</td>
    </tr>
    <tr>
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>jewish</td>
      <td>Whether a participant describes him or herself as Jewish.</td>
      <td>Yes<br>No<br>Unknown</td>
    </tr>
    <tr>
      <td>other_race</td>
      <td>Racial designation not matching one of the enumerated racial categories.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>participants.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>participants.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>principal_tribe_community</td>
      <td>Principal tribe or community not matching one of the enumerated racial categories.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>project_id</td>
      <td>Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>race</td>
      <td>What is your race? SELECT ALL THAT APPLY</td>
      <td>White<br>Black or African American<br>American Indian or Alaska Native (SPECIFY principal tribe or community)<br>Native Hawaiian or Other Pacific Islander<br>Asian<br>Some other race (SPECIFY)<br>Not reported</td>
    </tr>
    <tr>
      <td>state</td>
      <td>The current state of the object.</td>
      <td>uploading<br>uploaded<br>md5summing<br>md5summed<br>validating<br>error<br>invalid<br>suppressed<br>redacted<br>live<br>validated<br>submitted<br>released</td>
    </tr>
    <tr>
      <td>submitter_id</td>
      <td>No description</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>type</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>updated_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>vital_statistics_for_count_of_overdose_deaths</td>
      <td>tbd</td>
      <td>string</td>
    </tr>
    <tr>
      <td>year_of_birth</td>
      <td>Numeric value to represent the calendar year in which an individual was born.</td>
      <td>number<br>null</td>
    </tr>
  </tbody>
</table>